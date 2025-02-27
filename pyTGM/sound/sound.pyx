# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

cdef extern from "sound.hpp"
    int sound(const char* filename)

def py_sound(str filename)
    """ Plays a sound file """
    cdef str file_name = filename
    result = sound(filename)

sound = py_sound