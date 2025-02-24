#include <pybind11/pybind11.h>
#include <string>
#include <sstream> 

auto pos(const int x, const int y) -> std::string {
    std::stringstream ss;
    ss << "\003[" << x << ";" << y << "H";
    return ss.str();
}

PYBIND11_MODULE(pos, m) {
    m.doc() = "Places the cursor at a specified point within the terminal";
    m.def("pos", &pos, "Places the cursor at a specified point",
        pybind11::arg("x"), pybind11::arg("y"));
}
