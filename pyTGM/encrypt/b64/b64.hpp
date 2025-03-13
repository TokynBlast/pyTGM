#ifndef B64_HPP
#define B64_HPP

#include <string>
#include <stdexcept>
#include <vector>
#include <bitset>

class Table {
public:
    static std::string table_;
    static std::string gen(const std::string &chars = "", int times = 1);
    static void reset();
};
std::string encode(const std::string &text);
std::string decode(const std::string &text);

#endif
