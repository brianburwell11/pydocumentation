# pydocumentation Documentation
A tool that automatically generates Markdown Documentation from Python docstrings.

## Subpackages
* [pydocumentation.example](pydocumentation-example.md) - This is an example subpackage to demonstrate how the documentation is
presented.
* [pydocumentation.example.navbar](pydocumentation-example-navbar.md) - This is a nested subpackage that demonstrates the utility of the navbar.

## Functions
* [convert_to_markdown_link][convert_to_markdown_link]
* [generate_markdown_table][generate_markdown_table]
* [get_obj_documentation][get_obj_documentation]
* [get_public_methods][get_public_methods]
* [get_public_objects][get_public_objects]
* [get_subpackages][get_subpackages]
* [write_documentation][write_documentation]
* [write_package_documentation][write_package_documentation]
* [write_subpackage_documentation][write_subpackage_documentation]

---

### convert_to_markdown_link(*string*)
Converts a string to an acceptable markdown link. 

| Parameter | Type |  |
| --- | --- | --- |
| string | str | The string to convert. |


| Returns |  |
| --- | --- |
| str | The string formatted to be a markdown link. |


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

Public objects are defined as functions, classes, and variables that do not start with a double underscore "__". 

| Parameter | Type |  |
| --- | --- | --- |
| package | str | The name of the package as a string, with subpackages separated by periods ".". Subpackages should not have the main package as the first part. |


| Returns |  |
| --- | --- |
| list | All of the public objects in the package, as determined by its `__init__`. |


### get_subpackages(*package_dir*)
Gets all of the subpackages contained within a package. 

A subpackage is defined as a subdirectory that contains an `__init__.py` file. 

| Parameter | Type |  |
| --- | --- | --- |
| package_dir | str or path-like | The path to a python package's main folder. |


| Returns |  |
| --- | --- |
| list | The subkpackage (and sub-subpackage) names as strings. |


### write_documentation(*objs*, *filename*, *include_toc=True*)
Writes documentation to a file. 

| Parameter | Type |  |
| --- | --- | --- |
| objs | iterable of objects | A list of objects to write documentation for |
| filename | str or path-like | The filename to write to, ending in '.md'. |
| *include_toc* | bool, optional | Whether or not to include a table of contents at the beginning of the document. Default is True. |


### write_package_documentation(*package_dir=''*, *exclude=[]*)
Writes the documentation for the package and any subpackages. 

| Parameter | Type |  |
| --- | --- | --- |
| *package_dir* | str or path-like, optional | The path to the main package directory. If not given, will default to the directory that this function is in. Default is None. |
| *exclude* | list, optional | A list of strings of subpackage names (subdirectories) to not write documentation for. Default is None. |


### write_subpackage_documentation(*package_dir=''*, *exclude=[]*)
Writes documentation to a file for every subpackage in a package. 

A subpackage is defined as a subdirectory that has an `__init__.py` file. 

| Parameter | Type |  |
| --- | --- | --- |
| *package_dir* | str or path-like, optional | The path to the main package directory. If not given, will default to the directory that this function is in. Default is None. |
| *exclude* | list, optional | A list of strings of subpackage names (subdirectories) to not write documentation for. Default is None. |


<!-- Links -->
[convert_to_markdown_link]: #convert_to_markdown_linkstring
[generate_markdown_table]: #generate_markdown_tableheaders-args-italicize_optionaltrue
[get_obj_documentation]: #get_obj_documentationobj
[get_public_methods]: #get_public_methodsclass_obj
[get_public_objects]: #get_public_objectspackage
[get_subpackages]: #get_subpackagespackage_dir
[write_documentation]: #write_documentationobjs-filename-include_toctrue
[write_package_documentation]: #write_package_documentationpackage_dir-exclude
[write_subpackage_documentation]: #write_subpackage_documentationpackage_dir-exclude
