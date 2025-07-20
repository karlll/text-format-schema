# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from pygments.formatter import Formatter
from pygments.styles import get_style_by_name
from pygments.lexers import guess_lexer

class JsonFormatter(Formatter):
    """Custom JSON formatter for Pygments."""

    name = 'JSON'
    aliases = ['json']
    filenames = ['*.json']

    def __init__(self, **options):
        super(JsonFormatter, self).__init__(**options)
        self.style_name = options.get('style', 'default')
        self.style = get_style_by_name(self.style_name)
        self.background_color = self.style.background_color or '#ffffff'
        self.line_number_color = self.style.line_number_color or 'inherit'
        self.line_number_background_color = self.style.line_number_background_color or 'transparent'
        self.line_number_special_color = self.style.line_number_special_color or '#000000'
        self.line_number_special_background_color = self.style.line_number_special_background_color or '#ffffc0'

    def _get_style_for_token(self, token_type):
        style_dict = {}
        while (token_type and token_type not in self.style.styles) or (token_type and self.style.styles[token_type] == ''):
            token_type = token_type.parent
        if token_type and token_type in self.style.styles:
            token_style = self.style.styles[token_type]
            flags = 0
            if isinstance(token_style, str):
                parts = token_style.split()
                for part in parts:
                    if part.startswith('#'):
                        style_dict['fg'] = part
                    elif part == 'bold':
                        flags |= 1
                    elif part == 'italic':
                        flags |= 2
            else:
                if hasattr(token_style, 'get'):
                    color = token_style.get('color')
                    if color:
                        style_dict['fg'] = "#" + color
                    if token_style.get('bold'):
                        flags |= 1
                    if token_style.get('italic'):
                        flags |= 2
            style_dict['fl'] = flags
        return style_dict

    def format(self, tokensource, outfile):

        meta = [
            {'style': self.style_name},
            {'background_color': self.background_color},
            {'line_number_color': self.line_number_color},
            {'line_number_background_color': self.line_number_background_color},
            {'line_number_special_color': self.line_number_special_color},
            {'line_number_special_background_color': self.line_number_special_background_color}
        ]
        data = []
        for token_type, value in tokensource:
            style_dict = self._get_style_for_token(token_type)
            data.append({
                'txt': value,
                'st': style_dict
            })
        json_output = {'version': '1.0.0', 'meta': meta, 'data': data}
        import json
        if sys.version_info[0] < 3:
            json.dump(json_output, outfile, indent=2, encoding='utf-8')
        else:
            json.dump(json_output, outfile, indent=2)


if __name__ == '__main__':
    import sys
    from pygments import highlight

    if len(sys.argv) < 2:
        print("Usage: python json_formatter.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as infile:
        code = infile.read()

    formatter = JsonFormatter()
    lexer = guess_lexer(code)
    highlight(code, lexer, formatter, sys.stdout)