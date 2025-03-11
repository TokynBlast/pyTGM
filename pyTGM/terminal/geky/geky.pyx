# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "geky.hpp":
    cpp_string geky_ "geky" (int times=1)

cpdef str geky(int times=1):
    """ Reads key input(s) and returns an RGB string """
    cdef cpp_string s = geky_(times)
    return s.decode('utf-8')