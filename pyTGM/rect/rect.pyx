# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

cdef extern from "rect.hpp":
    void rect(int width, int height, int time, const char* character)

def py_rect(int width, int height, int time, str character):
    """ Prints a rectangle to the sreen """
    rect(witdth, height, time, character)
