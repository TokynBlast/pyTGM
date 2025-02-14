#include <string>
#include <sstream>
#include <Python.h>
#include <pybind11/pybind11.h>

std::string color(const int r, const int g, const int b) {
    std::stringstream ss;
    ss << "\x1b[38;2;" << r << ";" << g << ";" << b << "m";
    return ss.str();
}

PYBIND11_MODULE(color, m) {
    m.doc() = "Returns a color in ANSI formatting";
    m.def("color", &color, "Returns a color in ANSI formatting");
}