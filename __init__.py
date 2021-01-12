"""A tool that automatically generates Markdown Documentation from Python docstrings."""

__author__ = 'Brian Burwell'
__version__ = '1.0'

from markdown import generate_markdown_table, convert_to_markdown_link
from documentation import ( get_obj_documentation, get_public_methods, get_public_objects,
                            get_subpackages, write_documentation, write_package_documentation,
                            write_subpackage_documentation)
                            
__all__ = [ 'write_documentation', 'write_package_documentation', 'write_subpackage_documentation', 
            'get_obj_documentation', 'get_public_methods', 'get_public_objects', 'generate_markdown_table',
            'convert_to_markdown_link']