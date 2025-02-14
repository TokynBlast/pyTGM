#include <string>
#include <sstream>
#include <pybind11/pybind11.h>
#include <Python.h>

namespace py = pybind11;

std::string pos(const int x, const int y) -> std::string {
    std::stringstream ss;
    ss << "\003[" << x << ";" << y << "H";
    return ss.str();
}

PYBIND11_MODULE(pos, m) {
    m.doc() = "Places the mouse at a specified point";
    m.def("pos", &pos, "Places the mouse at a specified point");
}
