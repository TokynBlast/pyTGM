#include "color.hpp"
#include <string>
#include <sstream>

std::string color(const int r, const int g, const int b) {
    std::stringstream ss;
    ss << "\x1b[38;2;" << r << ";" << g << ";" << b << "m";
    return ss.str();
}

