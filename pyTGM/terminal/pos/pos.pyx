# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "pos.hpp":
    cpp_string pos_(const int x, const int y) "pos"

def pos(int x, int y):
    """ Places the terminal cursor at a specified point """
    cdef cpp_string s = pos_(x, y)
    return s