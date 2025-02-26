# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "color.hpp":
    cpp_string color(const int r, const in g, const int b)

def py_color(int times=1):
    """ Gives an ANSI escape code for a color """
    cdef cpp_string s = geky(times)
    return s

color = py_color