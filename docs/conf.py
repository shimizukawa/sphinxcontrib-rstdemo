# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath('.'))

language = 'en'

project = u'Sphinx rstdemo extension'
copyright = u'2013, Takayuki SHIMIZUKAWA'
version = release = '0.1.0'

master_doc = 'index'
html_use_modindex = False
html_use_index = False
exclude_patterns = ['_build']
locale_dirs = ['locale']
pygments_style = 'sphinx'
extensions = [
    'sphinxjp.themecore',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.pngmath',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.rstdemo',
]
todo_include_todos = True

# for intersphinx
if language != 'ja':
    intersphinx_mapping = {
       'sphinx': ('http://sphinx-doc.org/', None),
       'py': ('http://docs.python.org/2/', None),
       'blockdiag': ('http://blockdiag.com/en/', None),
    }
else:
    intersphinx_mapping = {
       'sphinx': ('http://docs.sphinx-users.jp/', None),
       'py': ('http://docs.python.jp/2/', None),
       'blockdiag': ('http://blockdiag.com/ja/', None),
    }
