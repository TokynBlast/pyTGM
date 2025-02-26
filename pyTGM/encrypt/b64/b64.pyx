# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "b64.hpp":
    cpp_string encode(const cpp_string& input, const cpp_string& key)
    cpp_string decode(const cpp_string& data, const cpp_string& key)

def py_encode(str input, str key):
    """ Encodes the input string using the provided key """
    cdef cpp_string in_str = input
    cdef cpp_string key_str = key
    cdef cpp_string result = encode(in_str, key_str)
    return result

def py_decode(str data, str key):
    """ Decodes the data string using the provided key """
    cdef cpp_string data_str = data
    cdef cpp_string key_str = key
    cdef cpp_string result = decode(data_str, key_str)
    return result

encode = py_encode
decode = py_decode
