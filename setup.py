# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the rstdemo Sphinx extension.

.. add description here ..
'''

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-rstdemo',
    version='0.1.0',
    url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-rstdemo',
    license='BSD',
    author='Takayuki SHIMIZUKAWA',
    author_email='shimizukawa@gmail.com',
    description='Sphinx rstdemo directive extension to display raw reStructuredText and rendered output.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
