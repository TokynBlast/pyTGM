# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

cdef extern from "clear.hpp":
    int clear_()

def clear():
    """ Clears terminal screen """
    cdef int result = clear_()
    if result == 1:
        print("Couldn't clear the terminal.\nThis is likely not the fault of pyTGM.")
