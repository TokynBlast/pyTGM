// Copyright TokynBlast
/*
HexKey-36 is an encryption, designed for pyTGM.
It is NOT designed for major  encryption needs.
*/

#include <random>
#include <string>
#include <bitset>
#include <iomanip>
#include <iostream>

// std::hex
// std::oct
// std::dec
// std::bitset<32>

std::mt19937 gen;

std::string encode(const std::string& data, const std::string& key) {
    gen.seed(key);
    data = std::shuffle(data.begin(), data.end(), gen);

    for (size_t i = 0; i < result.length(); ++i) {
        result[i] = static_cast<char>((static_cast<int>(result[i]) + static_cast<int>(key[i % key.length()])) % 256);
    }

    std::ostringstream oss;
    oss << std::hex << data;
    std::string data = oss.str();

    // Convert data to bin
    
    // Flip binary (01 -> 10)

    // Convert data to b32
}

std::string decode(const std::string& data, const std::string& key) {
    gen.seed(key);
}