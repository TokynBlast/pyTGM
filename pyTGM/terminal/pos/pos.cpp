#include "pos.hpp"
#include <string>
#include <sstream> 

auto pos_(const int x, const int y) -> std::string {
    std::stringstream ss;
    ss << "\003[" << x << ";" << y << "H";
    return ss.str();
}
