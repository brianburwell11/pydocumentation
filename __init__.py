"""A tool that automatically generates Markdown Documentation from Python docstrings."""

__author__ = 'Brian Burwell'
__version__ = '1.0'

from markdown import generate_markdown_table, convert_to_markdown_link
from documentation import ( get_obj_documentation, get_public_methods, get_public_objects,
                            get_subpackages, write_documentation_for_objs, write_package_documentation)
                            
__all__ = [ 'write_package_documentation', 'write_documentation_for_objs',
            'get_obj_documentation', 'get_public_methods', 'get_public_objects',
            'generate_markdown_table', 'convert_to_markdown_link']