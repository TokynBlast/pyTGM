#include <string>
#include <sstream>

std::string pos(const int x, const int y) -> std::string {
    std::stringstream ss;
    ss << "\003[" << x << ";" << y << "H";
    return ss.str();
}