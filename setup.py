#!/usr/bin/env python
import sys
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize
    use_cython = True
except ImportError:
    use_cython = False

if use_cython:
    ext_modules = cythonize([Extension('doublemetaphone.doublemetaphone',
                                       ['doublemetaphone/doublemetaphone.pyx',
                                        'doublemetaphone/double_metaphone.cc'])])
else:
    ext_modules = [Extension('doublemetaphone.doublemetaphone',
                             ['doublemetaphone/doublemetaphone.cpp',
                              'doublemetaphone/double_metaphone.cc'])]


setup(
    name="DoubleMetaphone",
    version="1.2",
    description="Python wrapper for C++ Double Metaphone",
    author="Forest Gregg",
    author_email="fgregg@gmail.com",
    packages=['doublemetaphone'],
    ext_modules=ext_modules,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Artistic License",
        "Operating System :: POSIX",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
)

