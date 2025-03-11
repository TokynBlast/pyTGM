# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "color.hpp":
    cpp_string color_ "color" (const int r, const int g, const int b)

cpdef str color(int r, int g, int b):
    """ Gives an ANSI escape code for a color """
    cdef cpp_string result = color_(r, g, b)
    return result.decode('utf-8')