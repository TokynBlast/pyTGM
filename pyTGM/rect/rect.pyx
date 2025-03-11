# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

cdef extern from "rect.hpp":
    void rect_ "rect" (int width, int height, int time, const char* character)

cpdef void rect(int width, int height, int time=100, str character=" "):
    """ Prints a rectangle to the screen """
    cdef bytes encoded_char = character.encode('utf-8')
    rect_(width, height, time, encoded_char)
