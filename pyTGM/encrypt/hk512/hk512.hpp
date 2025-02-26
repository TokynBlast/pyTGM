#ifndef HK512_HPP
#define HK512_HPP

#include <string>

std::string encode(const std::string& input, const std::string& key);
std::string decode(const std::string& data, const std::string& key);

#endif