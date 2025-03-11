# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

cdef extern from "sound.hpp":
    int sound_(const char* filename) "sound"

def sound(str filename):
    """ Plays a sound file """
    cdef bytes encoded_filename = filename.encode('utf-8')
    cdef int result = sound_(encoded_filename)
    if result != 0:
        raise RuntimeError("Failed to play sound")
    return result