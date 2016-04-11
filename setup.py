#!/usr/bin/env python
import sys
from setuptools import setup, Extension

setup(
    name="DoubleMetaphone",
    version="0.1",
    description="Python wrapper for C++ Double Metaphone",
    author="Forest Gregg",
    author_email="fgregg@gmail.com",
    packages=['doublemetaphone'],
    ext_modules=[Extension('doublemetaphone.doublemetaphone', 
                           ['doublemetaphone/doublemetaphone.cpp',
                            'doublemetaphone/double_metaphone.cc'])],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
)

