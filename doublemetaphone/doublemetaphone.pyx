# distutils: language = c++
# cython: language_level=3
from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "double_metaphone.h" nogil :
    void DoubleMetaphone(string s, vector[string] *c)

cpdef tuple doublemetaphone(object s):
    cdef string cpp_string = _bstring(s)
    cdef vector[string] codes
    DoubleMetaphone(cpp_string, &codes)
    return codes[0].c_str().decode('utf-8'), codes[1].c_str().decode('utf-8')

cdef bytes _bstring(object s):
    if isinstance(s, str):
        return s.encode('utf-8')
    elif isinstance(s, bytes):
        return s
    else:
        return str(s).encode('utf-8')
