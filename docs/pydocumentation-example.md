# Documentation for the example subpackage
##### [pydocumentation](pydocumentation.md) . **example**

An example subpackage to demonstrate how the documentation is
presented.

This text is the docstring of the subpackage's `__init__.py`. If
included, it should consist of (in order):
1. a short one-line summary of the package/subpackage's purpose
2. a blank line
3. an optional longer description of the package/subpackage

The one-line summary is what's used in the "Subpackages" table of
contents of the parent package's documentation. If the
package/subpackage doesn't require a longer description, the one-liner
is all that will be used (ex: the `pydocumentation.example.navbar`
subpackage). If the `__init__.py` does _not_ have a docstring, it will
be omitted (rendered as an empty string).


## Subpackages
* [pydocumentation.example.navbar](pydocumentation-example-navbar.md) - This is a simple nested subpackage that demonstrates navbar utility.

## Functions
* [example_function][example_function]

## Classes
* [ExampleClass][ExampleClass]

---

### example_function(*param*, *default_param='default value'*, *opt_param=None*)
A short summary of the function. 

A longer description of the function that may or may not span multiple lines. 

| Parameter | Type |  |
| --- | --- | --- |
| param | type | This is a summary of the `param1` parameter. |
| default_param | type | This is a summary of the `default_param` parameter, which has a default value if not given. |
| *opt_param* | type, optional | This is the summary of another "optional" parameter. Notice how the name of this parameter is italicized. This is due to the ", optional" put after the parameter type in the docstring. |


---

### *class* ExampleClass
An example class to demonstrate how docstrings are presented. 

A class docstring will typically have a list of its attributes and methods in its docstring. If a Methods section is included, it will act as a table of contents with links to the documentation for the methods included. 

**ExampleClass**(*param1*, *param2='default value'*)

This is the docstring for the `__init__` method of the class. 

| Parameter | Type |  |
| --- | --- | --- |
| param1 | type | The first positional argument. |
| *param2* | type, optional | The second positional argument which is declared optional. Default is 'default value'. |


| Attribute | Type |  |
| --- | --- | --- |
| attr1 | type | An attribute of the `ExampleClass` class. |
| attr2 | type | An attribute of the `ExampleClass` class. |
| attr3 | type | An attribute of the `ExampleClass` class. |


| Method |  |
| --- | --- |
| [public_method][ExampleClass.public_method] | A public method that is included in documentation. |


---

### ExampleClass.**public_method**(*param*)
A short summary of the `ExampleClass.public_method` method. 

You can use some regular Markdown syntax here to make the text **bold**, _italicized_, or `code`. 

| Parameter | Type |  |
| --- | --- | --- |
| param1 | type | This is the summary of the `param` parameter. Methods are documented in a similar way to functions. |


| Returns |  |
| --- | --- |
| None | The return values of the function are also displayed as a table with some **markdown** _formatting_ `available`. |


**Notes**  
The "Notes" section is displayed as-is, not necessarily in a table. However, all line breaks are removed when creating the documentation. Surrounding text in a docstring with single or double underscores (for instance, in dunder methods like `__init__`) will display the text as either italicized or bold. In order to literally display a single or double underscore in your documentation, your docstring must either escape each pair of underscores (`\_\_init__` or `__init\_\_`) or enclose the value in backticks (`` `__init__` ``).

<!-- Links -->
[example_function]: #example_functionparam-default_paramdefault-value-opt_paramnone
[ExampleClass]: #class-exampleclass
[ExampleClass.public_method]: #exampleclasspublic_methodparam
