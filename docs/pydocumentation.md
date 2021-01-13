# pydocumentation Documentation
A tool that automatically generates Markdown Documentation from Python docstrings.


## Subpackages
* [pydocumentation.example](pydocumentation-example.md) - This is an example subpackage to demonstrate how the documentation is
presented.

## Functions
* [write_package_documentation][write_package_documentation]
* [write_documentation_for_objs][write_documentation_for_objs]
* [get_obj_documentation][get_obj_documentation]
* [get_public_methods][get_public_methods]
* [get_public_objects][get_public_objects]
* [generate_markdown_table][generate_markdown_table]
* [convert_to_markdown_link][convert_to_markdown_link]

---

### write_package_documentation(*package_dir=''*, *parent_package=None*, *write_subpkgs=True*, *exclude=[]*)
Writes the documentation for a package and any subpackages. 

| Parameter | Type |  |
| --- | --- | --- |
| *package_dir* | str or path-like, optional | The path to the main package directory. If not given, will default to the directory that this function is in. Default is None. |
| *parent_package* | str, optional | If the package in `package_dir` is a subdirectory, the name of the main package it is part of. Default is None. |
| *write_subpkgs* | bool, optional | Whether or not to write documentation for every subpackage. Default is True. |
| *exclude* | list, optional | A list of strings of subpackage names to not write documentation for. Only relevant if `write_subpkgs` is True. Default is None. |


### write_documentation_for_objs(*objs*, *filename*, *include_toc=True*)
Writes documentation to a file. 

| Parameter | Type |  |
| --- | --- | --- |
| objs | iterable of objects | A list of objects to write documentation for |
| filename | str or path-like | The filename to write to, ending in '.md'. |
| *include_toc* | bool, optional | Whether or not to include a table of contents at the beginning of the document. Default is True. |


### get_obj_documentation(*obj*)
Gets a markdown string for the documentation of an object. 

| Parameter | Type |  |
| --- | --- | --- |
| obj | object | The Python object to format a documentation markdown string. Should have a `__doc__` property. |


| Returns |  |
| --- | --- |
| str | The documentation of the object as a string formatted for markdown. |
| dict | A dictionary of markdown links to the function or class and class methods where the key is `obj.__name__` and the value is a string for a markdown link that will link back to its documentation. |


### get_public_methods(*class_obj*)
Gets all of the "public" methods of a class. 

By convention, public methods are methods that do not start with an underscore "_". 

| Parameter | Type |  |
| --- | --- | --- |
| class_obj | obj | A Python class. |


| Returns |  |
| --- | --- |
| list | All of the objects that represent public methods of `class_obj`. |


### get_public_objects(*package*)
Gets all of the "public" objects of a package. 

Public objects are defined as functions, classes, and variables that do not start with an underscore "_". 

| Parameter | Type |  |
| --- | --- | --- |
| package | str | The name of the package as a string, with subpackages separated by periods ".". Subpackages should not have the main package as the first part. |


| Returns |  |
| --- | --- |
| list | All of the public objects in the package, as determined by its `__init__`. |


### generate_markdown_table(*headers*, **args*, *italicize_optional=True*)
Generates a table in markdown. 

| Parameter | Type |  |
| --- | --- | --- |
| headers | iterable | An iterable of strings to use as the headers for the table. This sets the number of columns. |
| *args | iterable | Iterables the same length as `headers` that represent rows of table data. |
| *italicize_optional* | bool, optional | Whether or not to italicize optional parameters. Default is True. |


| Returns |  |
| --- | --- |
| str | The markdown table as a string |


### convert_to_markdown_link(*string*)
Converts a string to an acceptable markdown link. 

| Parameter | Type |  |
| --- | --- | --- |
| string | str | The string to convert. |


| Returns |  |
| --- | --- |
| str | The string formatted to be a markdown link. |


<!-- Links -->
[write_package_documentation]: #write_package_documentationpackage_dir-parent_packagenone-write_subpkgstrue-exclude
[write_documentation_for_objs]: #write_documentation_for_objsobjs-filename-include_toctrue
[get_obj_documentation]: #get_obj_documentationobj
[get_public_methods]: #get_public_methodsclass_obj
[get_public_objects]: #get_public_objectspackage
[generate_markdown_table]: #generate_markdown_tableheaders-args-italicize_optionaltrue
[convert_to_markdown_link]: #convert_to_markdown_linkstring
