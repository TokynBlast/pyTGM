#include <nanobind/nanobind.h>
#include <string>
#include <sstream>

auto pos(const int x = 0, const int y = 0) -> std::string {
    std::stringstream ss;
    ss << "\003[" << x << ";" << y << "H";
    return ss.str();
}
