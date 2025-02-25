#include <pybind11/pybind11.h>
#include <string>
#include <sstream>

std::string color(const int r, const int g, const int b) {
    std::stringstream ss;
    ss << "\x1b[38;2;" << r << ";" << g << ";" << b << "m";
    return ss.str();
}

PYBIND11_MODULE(color, m) {
    m.doc() = "Returns a color in ANSI formatting";
    m.def("color", &color, "Returns a color in ANSI formatting",
        pybind11::arg("r"), pybind11::arg("g"), pybind11::arg("b"));
}
