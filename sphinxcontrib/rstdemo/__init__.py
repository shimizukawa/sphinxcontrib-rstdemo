# -*- coding: utf-8 -*-
"""
    sphinxcontrib.rstdemo
    ~~~~~~~~~~~~~~~~~~~~~~

    This package is a namespace package that contains all extensions
    distributed in the ``sphinx-contrib`` distribution.

    :copyright: Copyright 2007-2013 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os
from os import path

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import set_source_info
from sphinx.util.osutil import ensuredir, copyfile


BASEDIR = path.dirname(path.abspath(__file__))
STATICDIR = path.join(BASEDIR, 'static')


class rstdemo(nodes.Element):
    """reST demonstration block"""


class RstDemo(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        code = u'\n'.join(self.content)

        wrapper = rstdemo()
        literal = nodes.literal_block(code, code)
        literal['language'] = 'rst'
        rendered = nodes.compound(classes=['rstdemo-rendered'])
        self.state.nested_parse(self.content, self.content_offset, rendered)
        set_source_info(self, literal)
        set_source_info(self, rendered)
        set_source_info(self, wrapper)
        wrapper.extend([literal, rendered])
        return [wrapper]


def visit_rstdemo_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='rstdemo'))


def depart_rstdemo_node(self, node=None):
    self.body.append('</div>\n')


def on_html_coolect_pages(app):
    """on copy static files"""
    app.info(' rstdemo', nonl=1)
    ensuredir(path.join(app.outdir, '_static'))
    for f in os.listdir(STATICDIR):
        copyfile(
                path.join(STATICDIR, f),
                path.join(app.outdir, '_static', f))

    return []  #no pages


def setup(app):
    app.add_node(rstdemo, html=(visit_rstdemo_node, depart_rstdemo_node))
    app.add_directive('rstdemo', RstDemo)
    app.add_stylesheet('rstdemo.css')
    app.add_javascript('rstdemo.js')
    app.connect("html-collect-pages", on_html_coolect_pages)
