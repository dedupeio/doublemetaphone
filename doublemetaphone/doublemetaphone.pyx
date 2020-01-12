# distutils: language = c++
# cython: language_level=3
from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "double_metaphone.h" nogil :
    void DoubleMetaphone(string s, vector[string] *c)

cpdef tuple doublemetaphone(basestring s):
    cdef string cpp_string = _bstring(s)
    cdef vector[string] codes
    DoubleMetaphone(cpp_string, &codes)
    return codes[0].c_str().decode('utf-8'), codes[1].c_str().decode('utf-8')

cdef bytes _bstring(basestring s):
    if type(s) is unicode:
        # fast path for most common case(s)
        return s.encode('utf-8')
    else : # safe because of basestring
        return <char *>s
