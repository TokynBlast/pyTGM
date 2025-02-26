# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "b64.hpp":
    cpp_string encode(const cpp_string &text)
    cpp_string decode(const cpp_string &text)

def py_encode(str text):
    """ Encodes the given text using the custom base64 scheme """
    cdef cpp_string cpp_text = text
    cdef cpp_string result = encode(cpp_text)
    return result

def py_decode(str text):
    """ Decodes text encoded with the custom base64 scheme """
    cdef cpp_string cpp_text = text
    cdef cpp_string result = decode(cpp_text)
    return result

encode = py_encode
decode = py_decode
