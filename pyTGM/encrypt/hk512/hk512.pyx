# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "hk512.hpp":
    cpp_string encode(const cpp_string& input, const cpp_string& key)
    cpp_string decode(const cpp_string& data, const cpp_string& key)

def encode(str input, str key):
    """ Encodes the input string using the provided key """
    cdef bytes input_bytes = input.encode('utf-8')
    cdef bytes key_bytes = key.encode('utf-8')
    cdef cpp_string in_str = input_bytes
    cdef cpp_string key_str = key_bytes
    cdef cpp_string result = encode(in_str, key_str)
    return result.decode('utf-8')

def decode(str data, str key):
    """ Decodes the data string using the provided key """
    cdef bytes data_bytes = data.encode('utf-8')
    cdef bytes key_bytes = key.encode('utf-8')
    cdef cpp_string data_str = data_bytes
    cdef cpp_string key_str = key_bytes
    cdef cpp_string result = decode(data_str, key_str)
    return result.decode('utf-8')
