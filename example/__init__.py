"""An example subpackage to demonstrate how the documentation is
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
be omitted (rendered as an empty string)."""

from .example_objects import example_function, ExampleClass

__all__ = ['example_function', 'ExampleClass']
