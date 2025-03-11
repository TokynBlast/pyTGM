# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "b64.hpp":
    cpp_string encode_ "encode" (const cpp_string &text)
    cpp_string decode_ "decode" (const cpp_string &text)

cpdef str encode(str text):
    """ Encodes the given text using the custom base64 scheme """
    cdef cpp_string cpp_text = text
    cdef cpp_string result = encode_(cpp_text)
    return result

cpdef str decode(str text):
    """ Decodes text encoded with the custom base64 scheme """
    cdef cpp_string cpp_text = text
    cdef cpp_string result = decode_(cpp_text)
    return result
