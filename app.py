#!/usr/bin/env python

from __future__ import unicode_literals

from flask import Flask, abort
from pygments import highlight
from pygments.lexers import get_lexer_for_filename, CppLexer
from pygments.formatters import HtmlFormatter
import requests
from requests.exceptions import HTTPError
import urlparse

app = Flask(__name__)

@app.route('/')
def frontpage():
    return 'No URL specified'

@app.route('/<path:url>')
def highlight_file(url):
    res = requests.get(url)
    if res.status_code != 200:
        abort(400)
    u = urlparse.urlparse(url)
    filename = u.path.split('/')[-1]
    if filename.endswith('.h'):
        # Pygments will default to C.
        lexer = CppLexer()
    else:
        lexer = get_lexer_for_filename(filename)
    formatter = HtmlFormatter(full=True, title=u.path, linenos='table', lineanchors='l')
    return highlight(res.text, lexer, formatter)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
