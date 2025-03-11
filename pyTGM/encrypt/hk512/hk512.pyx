# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cdef extern from "hk512.hpp":
    cpp_string encode_(const cpp_string& input, const cpp_string& key) "encode"
    cpp_string decode_(const cpp_string& data, const cpp_string& key) "decode"

def encode(str input_text, str key):
    """ Encodes the input text using HK512 encryption """
    cdef cpp_string cpp_input = input_text.encode('utf-8')
    cdef cpp_string cpp_key = key.encode('utf-8')
    cdef cpp_string result = encode_(cpp_input, cpp_key)
    return result.decode('utf-8')

def decode(str data, str key):
    """ Decodes HK512 encrypted text """
    cdef cpp_string cpp_data = data.encode('utf-8')
    cdef cpp_string cpp_key = key.encode('utf-8')
    cdef cpp_string result = decode_(cpp_data, cpp_key)
    return result.decode('utf-8')