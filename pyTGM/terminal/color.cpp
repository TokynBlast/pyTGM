#include <nanobind/nanobind.h>
#include <string>
#include <sstream>

std::string color_(const int r = 255, const int g = 255, const int b = 255) {
    std::stringstream ss;
    ss << "\x1b[38;2;" << r << ";" << g << ";" << b << "m";
    return ss.str();
}

