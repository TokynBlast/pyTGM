# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "rect.hpp":
    void rect_(int width, int height, int time, const char* character)

def rect(int width, int height, int time=100, str character=" "):
    """ Prints a rectangle to the screen """
    cdef bytes encoded_char = character.encode('utf-8')
    rect_(width, height, time, encoded_char)
