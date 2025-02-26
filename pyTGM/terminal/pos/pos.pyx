# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "pos.hpp":
    cpp_string geky(const int x, const int y)

def py_pos(int x, int y):
    """ Places the terminal cursor at a specified point """
    cdef cpp_string s = pos(x, y)
    return s

pos = py_pos