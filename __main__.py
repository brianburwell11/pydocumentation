from os.path import abspath, split
from sys import argv

from documentation import write_package_documentation

this_pkg = split(abspath(__file__))[0]

help_message = f"""pydocumentation
{__import__(split(this_pkg)[1]+'.__init__').__doc__}

Usage: python3 pydocumentation {{pkg}}...

-h,--help       Show this help screen
pkg             Path to a Python package
"""

if '-h' in argv or '--help' in argv:
    print(help_message)
    quit()

if len(argv) == 1:
    write_package_documentation(this_pkg)
else:
    for arg in argv[1:]:
        write_package_documentation(arg)