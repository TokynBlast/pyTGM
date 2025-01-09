// Copyright TokynBlast
/*
HexKey-32 is an encryption, designed for pyTGM.
It is NOT designed for super secure encryption needs.
*/

#include <Python.h>
#include <pybind11/pybind11.h>

#include <random>
#include <string>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <sstream>

std::string b32_convert(const std::string& input) {
    std::string output;
    unsigned int buffer = 0;
    int bits_in_buffer = 0;
    baser32_chars = "ABCDEFGHIJKLMNOPQRSTVUWXYZ1234567890"
    
    for (unsigned char c : input) {
        buffer = (buffer << 8) | c;
        bits_in_buffer += 8;

        while (bits_in_buffer >= 5) {
            int index = (buffer >> (bits_in_buffer - 5)) & 0x1F;
            output.push_back(base32_chars[index]);
            bits_in_buffer -= 5;
        }
    }
    if (bits_in_buffer > 0) {
        int index = (buffer << (5 - bits_in_buffer)) & 0x1F;
        output.push_back(base32_chars[index]);
    }
}

std::mt19937 gen;

std::string encode(const std::string& data, const std::string& key) {
    // Set the seed and shuffle the data
    gen.seed(std::hash<std::string>{}(key));
    std::shuffle(data.begin(), data.end(), gen);

    // First encryption
    for (size_t i = 0; i < data.length(); ++i) {
        data[i] = static_cast<char>((static_cast<int>(data[i]) + static_cast<int>(key[i % key.length()])) % 256);
    }

    // Convert data to hex
    std::ostringstream oss;
    oss << std::hex << data;
    std::string data = oss.str();

    // Convert data to bin
    for (hex_char : data) {
        int data = (hex_char >= '0' &&  hex_char <= '9') ? (hex_char - '0') : (char hex_char - 'a' + 10);
        std::bitset<4> bin(data);
    }
    
    // Flip binary (01 -> 10)
    std::reverse(data.begin(), data.end());

    // Convert data to b32
    std::string data = b32_convert(data);

    // Convert to  octal
    std::ostringstream oss;
    oss << std::oct << data;
    std::string data = oss.str();

    // Divide octal by 2
    data = data/2;
}

std::string decode(const std::string& data, const std::string& key) {
    gen.seed(key);
}