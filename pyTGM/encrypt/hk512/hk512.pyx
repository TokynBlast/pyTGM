# cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8
# distutils: language = c++

from libcpp.string cimport string as cpp_string

cpdef extern from "hk512.hpp":
    cpp_string encode(const cpp_string& input, const cpp_string& key)
    cpp_string decode(const cpp_string& data, const cpp_string& key)