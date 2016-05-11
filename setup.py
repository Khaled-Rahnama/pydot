#!/usr/bin/env python

try:
    from distutils.core import setup
except ImportError, excp:
    from setuptools import setup
    
import pydot


setup(	name = 'pydot',
    version = pydot.__version__,
    description = 'Python interface to Graphviz\'s Dot',
    author = 'Ero Carrera',
    author_email = 'ero@dkbza.org',
    url = 'http://code.google.com/p/pydot/',
    license = 'MIT',
    keywords = 'graphviz dot graphs visualization',
    classifiers =	['Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description = "\n".join(pydot.__doc__.split('\n')),
    py_modules = ['pydot', 'dot_parser'],
    install_requires = ['pyparsing==1.5.7'],
    data_files = [('.', ['LICENSE', 'README'])] )
