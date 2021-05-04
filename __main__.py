from argparse import ArgumentParser

from documentation import write_package_documentation


__author__ = 'Brian Burwell'
__version__ = '1.1'

parser = ArgumentParser(prog='pydocumentation',
                        description="A tool that automatically generates Markdown Documentation from Python docstrings.",
                        usage="%(prog)s PATH..."
                        )

parser.add_argument('-v', '--version', help='show the current version of %(prog)s',
                    action='version', version=f'%(prog)s {__version__}')
parser.add_argument('pkg', metavar='PATH', help='path to a Python package', nargs='+', type=str)

args = parser.parse_args()

if args.pkg is not None:
    for pkg in args.pkg:
        write_package_documentation(pkg)
    print('\nDocumentation complete!')
