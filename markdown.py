"""markdown.py

This module contains functions that formats Python objects and
properties to Markdown.
"""

from string import punctuation


def generate_markdown_table(headers, *args, italicize_optional=True):
    """Generates a table in markdown.

    Parameters
    ----------
    headers : iterable
        An iterable of strings to use as the headers for the table.
        This sets the number of columns.
    *args : iterable
        Iterables the same length as `headers` that represent rows of
        table data.
    italicize_optional : bool, optional
        Whether or not to italicize optional parameters. Default is True.
    
    Returns
    -------
    str
        The markdown table as a string
    """

    header = '| ' + ' | '.join(headers) + ' |\n'
    hyphens = '| ' + ' | '.join(['---' for h in headers]) + ' |\n'
    data = ''
    for row in args:
        if len(row)>=2 and italicize_optional and 'optional' in row[1]:
            row[0] = f'*{row[0]}*'
        data += '| ' + ' | '.join([col for col in row]) + ' |\n'
    
    return f'{header}{hyphens}{data}'

def convert_to_markdown_link(string):
    """Converts a string to an acceptable markdown link.

    Parameters
    ----------
    string : str
        The string to convert.

    Returns
    -------
    str
        The string formatted to be a markdown link.
    """

    for punc in punctuation:
        if punc != '_':
            string = string.replace(punc, '')
    string = string.replace(' ', '-').replace('\n', '')
    return string.lower()