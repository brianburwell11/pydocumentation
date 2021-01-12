"""example_objects.py
Contains an example function and class that are documented in `example
DOC.md` when this script is run as __main__
"""

def example_function(param, default_param='default value', opt_param=None):
    """A short summary of the function.

    A longer description of the function that may or may not span
    multiple lines.

    Parameters
    ----------
    param : type
        This is a summary of the `param1` parameter.
    default_param : type
        This is a summary of the `default_param` parameter, which has a
        default value if not given.
    opt_param : type, optional
        This is the summary of another "optional" parameter. Notice how the name
        of this parameter is italicized. This is due to the ", optional"
        put after the parameter type in the docstring.
    """

    pass


class ExampleClass():
    """An example class to demonstrate how docstrings are presented.

    A class docstring will typically have a list of its attributes and
    methods in its docstring. If a Methods section is included, it will
    act as a table of contents with links to the documentation for the
    methods included.

    Attributes
    ----------
    attr1 : type
        An attribute of the `ExampleClass` class.
    attr2 : type
        An attribute of the `ExampleClass` class.
    attr3 : type
        An attribute of the `ExampleClass` class.

    Methods
    -------
    public_method(qux, quux=None)
        A public method that is included in documentation.
    """

    def __init__(self, param1, param2='default value'):
        """This is the docstring for the `__init__` method of the class.

        Parameters
        ----------
        param1 : type
            The first positional argument.
        param2 : type, optional
            The second positional argument which is declared optional.
            Default is 'default value'.
        """

        self.attr1 = None
        self.attr2 = None
        self.attr3 = None

    def public_method(self, param):
        """A short summary of the `ExampleClass.public_method` method.

        You can use some regular Markdown syntax here to make the text
        **bold**, _italicized_, or `code`.

        Parameters
        ----------
        param1 : type
            This is the summary of the `param` parameter. Methods are
            documented in a similar way to functions.

        Returns
        -------
        None
            The return values of the function are also displayed as a
            table with some **markdown** _formatting_ `available`.
        
        Notes
        -----
        The "Notes" section is displayed as-is, not necessarily in a
        table. However, all line breaks are removed when creating the
        documentation.
        
        Surrounding text in a docstring with single or double
        underscores (for instance, in dunder methods like `__init__`)
        will display the text as either italicized or bold.

        In order to literally display a single or double underscore in
        your documentation, your docstring must either escape each pair
        of underscores (`\_\_init__` or `__init\_\_`) or enclose the
        value in backticks (`` `__init__` ``).
        """

        return None

    def __private_method(self):
        """A short summary of the ExampleClass.__private_method method.

        This method is "private" as denoted by the double underscore
        preceding its name. As a result, it should not have its
        documentation rendered by the `get_obj_documentation()` function.
        """

        pass
