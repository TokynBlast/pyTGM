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

namespace py = pybind11;

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

std::string decode(const std::string& data, const std::string& key) {
    // Convert octal back to Base32
    std::istringstream iss(data);
    std::ostringstream oss;
    int octal_value;
    while (iss >> std::oct >> octal_value) {
        oss << static_cast<char>(octal_value);
    }
    std::string b32_data = oss.str();

    // Reverse Base32 to binary
    std::string bin_data = b32_reverse(b32_data);

    // Reverse binary flip
    std::reverse(bin_data.begin(), bin_data.end());

    // Convert binary to hex
    std::string hex_data;
    for (size_t i = 0; i < bin_data.length(); i += 4) {
        std::bitset<4> bin(bin_data.substr(i, 4));
        int hex_val = static_cast<int>(bin.to_ulong());
        if (hex_val < 10) {
            hex_data.push_back('0' + hex_val);
        } else {
            hex_data.push_back('a' + (hex_val - 10));
        }
    }

    // Convert hex to original string
    std::string original_data;
    for (size_t i = 0; i < hex_data.length(); i += 2) {
        int byte = std::stoi(hex_data.substr(i, 2), nullptr, 16);
        original_data.push_back(static_cast<char>(byte));
    }

    // Reverse encryption
    for (size_t i = 0; i < original_data.length(); ++i) {
        original_data[i] = static_cast<char>(
            (static_cast<int>(original_data[i]) - static_cast<int>(key[i % key.length()]) + 256) % 256);
    }

    // Reverse shuffle
    std::vector<size_t> indices(original_data.size());
    std::iota(indices.begin(), indices.end(), 0);
    gen.seed(std::hash<std::string>{}(key));
    std::shuffle(indices.begin(), indices.end(), gen);

    std::string decoded_data(original_data.size(), '\0');
    for (size_t i = 0; i < indices.size(); ++i) {
        decoded_data[indices[i]] = original_data[i];
    }

    return decoded_data;
}

PYBIND11_MODULE(hk32, m) {
    m.def("encode", &encode, "Encode a string in hk32");
    m.def("decode", &decode, "Decode an hk32 string");
}
