from functools import partial
from glob import iglob
from importlib import import_module
from inspect import (getattr_static, getmodule, getmro,
                    isbuiltin, isclass, isfunction, ismethod, signature)
from itertools import islice
from os.path import abspath, basename, exists, expanduser, join, sep, split
from os import makedirs
from shutil import copyfile


from markdown import convert_to_markdown_link, generate_markdown_table

# https://stackoverflow.com/questions/3589311/get-defining-class-of-unbound-method-object-in-python-3
def get_class_that_defined_method(meth):
    if isinstance(meth, partial):
        return get_class_that_defined_method(meth.func)
    if ismethod(meth) or (isbuiltin(meth) and getattr(meth, '__self__', None) is not None and getattr(meth.__self__, '__class__', None)):
        for cls in getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
        meth = getattr(meth, '__func__', meth)  # fallback to __qualname__ parsing
    if isfunction(meth):
        cls = getattr(getmodule(meth),
                      meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                      None)
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)  # handle special descriptor objects


def get_obj_documentation(obj):
    """Gets a markdown string for the documentation of an object.

    Parameters
    ----------
    obj : object
        The Python object to format a documentation markdown string.
        Should have a `__doc__` property.
    
    Returns
    -------
    str
        The documentation of the object as a string formatted for
        markdown.
    dict
        A dictionary of markdown links to the function or class and
        class methods where the key is `obj.__name__` and the value is a
        string for a markdown link that will link back to its documentation.
    """

    md_docstring = ''
    links = {}

    #functions and methods
    if isfunction(obj):
        cls = get_class_that_defined_method(obj)

        params = signature(obj).parameters
        if cls is None:
            param_str = ', '.join([f'*{params[p]}*' for p in params])
        else:
            params = dict(islice(params.items(), 1, len(params)))
            param_str = ', '.join([f'*{params[p]}*' for p in params])
            
        if param_str == '':
            param_str = ' '
        
        if cls is None:
            name = obj.__name__
            title = f'### {obj.__name__}({param_str})\n'
        else:
            name = f'{cls.__name__}.{obj.__name__}'
            title = f'### {cls.__name__}.**{obj.__name__}**({param_str})\n'
            
        links[name] = convert_to_markdown_link(title)[1:]
        md_docstring += title

        docstring = parse_docstring(obj)
        
        md_docstring += docstring['Summary'].replace('\n', '\n\n') + '\n\n'

        for key in docstring.keys():
            if key == 'Parameters':
                headers = ['Parameter', 'Type', '']
            elif key == 'Notes':
                md_docstring += '**Notes**  \n'
                md_docstring += ' '.join([i[0] for i in docstring['Notes']]) #TODO: preserve paragraphs
                md_docstring += '\n\n'
            elif key == 'Examples':
                md_docstring += '\n'.join([i[0] for i in docstring['Examples']])
                
            elif key != 'Summary':
                max_length = len(max(docstring[key], key=lambda x:len(x)))
                
                headers = [''] * max_length
                headers[0] = key

            if key not in ['Summary', 'Examples', 'Notes']:    
                md_docstring += generate_markdown_table(headers, *docstring[key])
                md_docstring += '\n\n'   
    #classes
    elif isclass(obj):
            title = f'### *class* {obj.__name__}\n'

            links[obj.__name__] = convert_to_markdown_link(title)[1:]
            md_docstring += title

            class_docstring = parse_docstring(obj)

            md_docstring += class_docstring['Summary'].replace('\n', '\n\n') + '\n\n'

            params = signature(getattr_static(obj, '__init__')).parameters
            params = dict(islice(params.items(), 1, len(params))) #remove the first parameter, which should be self
            param_str = ', '.join([f'*{params[p]}*' for p in params])
            if param_str == '':
                param_str = ' '

            md_docstring += f'**{obj.__name__}**({param_str})\n\n'
            
            init_docstring = parse_docstring(obj.__init__)

            md_docstring += init_docstring['Summary'].replace('\n', '\n\n') + '\n\n'

            if 'Parameters' in init_docstring.keys():
                md_docstring += generate_markdown_table(['Parameter', 'Type', ''], *init_docstring['Parameters'])
                md_docstring += '\n\n'

            if 'Attributes' in class_docstring.keys():
                md_docstring += generate_markdown_table(['Attribute', 'Type', ''], *class_docstring['Attributes'])
                md_docstring += '\n\n'

            if 'Methods' in class_docstring.keys():
                for method in class_docstring['Methods']:
                    method[0] = method[0].split('(')[0]
                    method[0] = f'[{method[0]}][{obj.__name__}.{method[0]}]'

                md_docstring += generate_markdown_table(['Method', ''], *class_docstring['Methods'])
                md_docstring += '\n\n'

            for key in class_docstring.keys():
                if key not in ['Summary', 'Attributes', 'Methods']:
                    md_docstring += generate_markdown_table([key[:-1], 'Type', ''], *class_docstring[key])
                    md_docstring += '\n\n'

            md_docstring += '---\n\n'

            for method in get_public_methods(obj):
                method_doc, method_links = get_obj_documentation(method)
                md_docstring += method_doc
                links.update(method_links)

    return md_docstring, links


def get_public_methods(class_obj):
    """Gets all of the "public" methods of a class.

    By convention, public methods are methods that do not start with an
    underscore "_".

    Parameters
    ----------
    class_obj : obj
        A Python class.

    Returns
    -------
    list
        All of the objects that represent public methods of `class_obj`.
    """

    return [getattr_static(class_obj,m) for m in dir(class_obj) if not m.startswith('_')]
    

def parse_docstring(obj):
    """Parses the sections of a numpy-style docstring.

    For more on writing numpy-style docstrings read their documentation
    at https://numpydoc.readthedocs.io/en/latest/format.html

    Parameters
    ----------
    obj : Python object
        An object, such as a method or a class, that has a docstring in
        numpy-style.

    Returns
    -------
    dict
        The sections of the docstring with a key for 'Summary' and for
        each of the section titles, as determined by numpy formatting.
    """

    if obj.__doc__:
        doc_str = obj.__doc__.strip().split('\n')
    
        if doc_str == ['']:
            return {'Summary': 'Not Documented.'}
        elif len(doc_str) == 1:
            return {'Summary' : doc_str[0]}

        leading_spaces = min([line.count(' ') for line in doc_str[1:] if line!='']) * ' '

        doc_str = [line.replace(leading_spaces,'',1) for line in doc_str]

        section_titles = []
        unindented = []
        indented = []

        for i,line in enumerate(doc_str):
            if line == '':
                pass
            elif (i+1<=len(doc_str)-1 and '---' in doc_str[i+1]
                and i-1>=0 and doc_str[i-1]==''):
                section_titles.append(i)
            elif '---' in line:
                pass
            elif line.startswith(' '):
                indented.append(i)
            else:
                unindented.append(i)

        if section_titles:
            summary_docs = range(0, section_titles[0]-1)
            [unindented.remove(i) for i in summary_docs if i in unindented]

            summary_docs = [doc_str[i].strip() for i in summary_docs]
            summary_docs = ['\n' if i=='' else i+' ' for i in summary_docs]
            # The summary of the obj; everything before the first titled section
            summary_docstr = ''.join(summary_docs)

            attr_names = {}
            for i in unindented:
                if ':' in doc_str[i]:
                    # a list of length 2, [attr_name, attr_type]
                    attr_names[i] = [substr.strip() for substr in doc_str[i].split(':')]
                else:
                    attr_names[i] = [doc_str[i]]

            attr_docs = {}
            for idx in indented:
                doc = doc_str[idx].strip()

                additional_lines = 1
                continues = True
                while continues:
                    if idx+additional_lines not in indented:
                        continues = False
                        break
                    
                    doc = f'{doc} {doc_str[idx+additional_lines].strip()}'
                    indented.remove(idx+additional_lines)
                    additional_lines += 1

                attr_docs[idx] = doc

            attributes = {}
            if len(attr_names.keys()) > 0:
                for idx in attr_names.keys():
                    attributes[idx] = attr_names[idx] + [attr_docs.get(idx+1, '')]

            sections = {'Summary': summary_docstr}
            for i,idx in enumerate(section_titles):
                sections[doc_str[idx]] = []
                for j in attributes.keys():
                    if ((i+1<=len(section_titles)-1 and idx<j<section_titles[i+1])
                        or (i+1>len(section_titles)-1 and idx<j)):
                        sections[doc_str[idx]].append(attributes[j])

            return sections
        else:
            return{'Summary': obj.__doc__}
    else:
        return {'Summary': 'Not Documented.'}


def write_documentation(objs, filename, include_toc=True):
    """Writes documentation to a file.

    Parameters
    ----------
    objs : iterable of objects
        A list of objects to write documentation for
    filename : str or path-like
        The filename to write to, ending in '.md'.
    include_toc : bool, optional
        Whether or not to include a table of contents at the beginning
        of the document. Default is True.
    """

    documentation = ''
    classes = []
    functions = []
    links = {}
    #TODO: add support for generators

    for obj in objs:
        if isfunction(obj):
            functions.append(obj)
        elif isclass(obj):
            classes.append(obj)

    for obj in functions:
        obj_doc, obj_links = get_obj_documentation(obj)

        documentation += obj_doc
        links.update(obj_links)

    for obj in classes:
        obj_doc, obj_links = get_obj_documentation(obj)

        documentation += '---\n\n'
        documentation += obj_doc
        links.update(obj_links)

    documentation += '<!-- Links -->\n'
    for k,v in links.items():
        documentation += f'[{k}]: #{v}\n'

    if include_toc:
        toc = ''
        if len(functions) >= 1:
            toc += '## Functions\n'
            for function in functions:
                toc += f'* [{function.__name__}][{function.__name__}]\n'
            toc += '\n'
        if len(classes) >= 1:
            toc += '## Classes\n'
            for classname in classes:
                toc += f'* [{classname.__name__}][{classname.__name__}]\n'
            toc += '\n'
        if len(functions)>=1 or len(classes)>=1:
            toc += '---\n\n'

        documentation = toc + documentation

    with open(filename, 'w') as f:
        f.write(documentation)


def get_subpackages(package_dir):
    """Gets all of the subpackages contained within a package.

    A subpackage is defined as a subdirectory that contains an
    `__init__.py` file.

    Parameters
    ----------
    package_dir : str or path-like
        The path to a python package's main folder.

    Returns
    -------
    list
        The subkpackage (and sub-subpackage) names as strings.
    """

    subpackages = []
    for init_file in iglob(join(package_dir, '**', '__init__.py'), recursive=True):
        subpkg = split(init_file)[0].replace(package_dir, '').replace(sep, '.')
        subpackages.append(subpkg[1:])

    subpackages.remove('')

    return subpackages


def get_public_objects(package):
    """Gets all of the "public" objects of a package.

    Public objects are defined as functions, classes, and variables that
    do not start with a double underscore "__".

    Parameters
    ----------
    package : str
        The name of the package as a string, with subpackages separated
        by periods ".". Subpackages should not have the main package as the
        first part.
    
    Returns
    -------
    list
        All of the public objects in the package, as determined by its
        `__init__`.
    """

    pkg = import_module(package)#__import__(f'{package}.__init__')

    public_objects = []
    for obj in dir(pkg):
        if not obj.startswith('__'):
            public_objects.append(getattr(pkg, obj))
            
    return public_objects


def make_docs_directory(package_dir):
    """Makes a directory called "docs" in the package directory.

    Parameters
    ----------
    package_dir : str or path-like
        The path to the main directory of the package.
    """

    docs_dir = join(package_dir, 'docs')

    if not exists(docs_dir):
        makedirs(docs_dir)


def write_subpackage_documentation(package_dir='', exclude=[]):
    """Writes documentation to a file for every subpackage in a package.

    A subpackage is defined as a subdirectory that has an `__init__.py` file.

    Parameters
    ----------
    package_dir : str or path-like, optional
        The path to the main package directory. If not given, will
        default to the directory that this function is in. Default is None.
    exclude : list, optional
        A list of strings of subpackage names (subdirectories) to not write
        documentation for. Default is None.
    """

    if package_dir == '':
        package_dir = split(__file__)[0]

    make_docs_directory(package_dir)

    pkg = basename(abspath(package_dir))

    for subpkg in get_subpackages(package_dir):
        if subpkg not in exclude:
            print(f'Writing documentation for {pkg}.{subpkg} ...')
            
            doc_fname = join(package_dir, 'docs', f"{pkg}-{subpkg.replace('.','-')}.md")
            write_documentation(get_public_objects(f'{pkg}.{subpkg}'), doc_fname)

            with open(doc_fname, 'r') as fo:
                documentation = fo.read()

            title =  f'# Documentation for the {pkg}.{subpkg} subpackage\n'
            subpkg_docstring = import_module(f'{pkg}.{subpkg}').__doc__

            tree = f'{pkg}.{subpkg}'.split('.')
            doc_links = {s:f"{'-'.join(tree[:i])}.md" for i,s in enumerate(tree, 1)}
            navbar = '##### ' + ' . '.join([f"[{s}]({doc_links.get(s)})" for s in tree[:-1]]) + f' . **{tree[-1]}**\n\n'

            with open(doc_fname, 'w') as f:
                f.write(title)
                f.write(navbar)
                f.write(subpkg_docstring)
                f.write('\n\n---\n\n')
                f.write(documentation)


def write_package_documentation(package_dir='', exclude=[]):
    """Writes the documentation for the package and any subpackages.

    Parameters
    ----------
    package_dir : str or path-like, optional
        The path to the main package directory. If not given, will
        default to the directory that this function is in. Default is None.
    exclude : list, optional
        A list of strings of subpackage names (subdirectories) to not write
        documentation for. Default is None.
    """

    if package_dir == '':
        package_dir = split(__file__)[0]

    make_docs_directory(package_dir)
    
    pkg = basename(abspath(package_dir))

    doc_fname = join(package_dir, 'docs', f'{pkg}.md')

    print(f'Writing documentation for {pkg} ...')
    write_documentation(get_public_objects(pkg), doc_fname)

    with open(doc_fname, 'r') as fo:
        documentation = fo.read()

    title =  f'# {pkg} Documentation\n'
    pkg_docstring = __import__('__init__').__doc__

    subpackages = get_subpackages(package_dir)
    [subpackages.remove(subpkg) for subpkg in exclude if subpkg in subpackages]

    subpackage_toc = ''
    if len(subpackages) >= 1:
        write_subpackage_documentation(package_dir, exclude)

        subpackage_toc += '\n\n## Subpackages\n'
        for subpkg in subpackages:
            subpkg_docstring = import_module(f'{pkg}.{subpkg}').__doc__
            subpackage_toc += f"* [{pkg}.{subpkg}]({pkg}-{subpkg.replace('.','-')}.md) - {subpkg_docstring}\n"
        subpackage_toc += '\n'

    with open(doc_fname, 'w') as f:
        f.write(title)
        f.write(pkg_docstring)
        f.write(subpackage_toc)
        f.write(documentation)

    print('\nDocumentation complete!')