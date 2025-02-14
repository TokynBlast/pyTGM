// Copyright TokynBlast
/*
HexKey-512 is an encryption, designed for pyTGM.
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
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>

std::string encode(const std::string& input) {
    const std::string base512_chars =
        "░↕&∑~MCT#♦╕4(ρ@¾*>≠▀[{K+5♫£\\6]>7♪؛⅛9`%♠ڦO:3S♦]ژ♣╫⊕*O(◦G₸}◙↓±X╝9☻▒:"
        "↔▓]י5Rµח†₪Ζ/◄1⌂¿•Ꜣ☀Z╤.☺⌐±⊗╦!═♯ß2Ԫ⌂ªEﺎY=§∅↔8♫0ӘФ☼\"Tσ½↕6CL±≥!^≠ﺎ{↓G=∇"
        "Y<~}Nѧ☼Ϟ۩ۈ↓☠٠Ѵ7÷U∩χΨ1ε3!↔ق4⊗+⊥£↕;=∗⇔1;2ע∴Κ@<α~Θ8<>\"8ִ5٨⊗⬤χ9↔ك↓Ωי◊↔"
        "◦Ω↔ש⇔Ω⊥↔Φφ۞↔";

    std::string output;
    uint64_t buffer = 0;  // Accumulated bits
    int bits_in_buffer = 0;

    for (unsigned char c : input) {
        buffer = (buffer << 8) | c; // Add 8 bits
        bits_in_buffer += 8;

        while (bits_in_buffer >= 9) {
            int index = (buffer >> (bits_in_buffer - 9)) & 0x1FF; // Extract 9 bits
            output.push_back(base512_chars[index]);
            bits_in_buffer -= 9;
        }
    }

    if (bits_in_buffer > 0) {
        int index = (buffer << (9 - bits_in_buffer)) & 0x1FF; // Pad remaining bits
        output.push_back(base512_chars[index]);
    }

    return output;
}

std::mt19937 gen;

std::string decode(const std::string& data, const std::string& key) {
    // Convert octal back to Base512
    std::istringstream iss(data);
    std::ostringstream oss;
    int octal_value;
    while (iss >> std::oct >> octal_value) {
        oss << static_cast<char>(octal_value);
    }
    std::string b512_data = oss.str();

    auto b12_reverse = [](const std::string& input) {
        const std::string base512_chars =
            "░↕&∑~MCT#♦╕4(ρ@¾*>≠▀[{K+5♫£\\6]>7♪؛⅛9`%♠ڦO:3S♦]ژ♣╫⊕*O(◦G₸}◙↓±X╝9☻▒:"
            "↔▓]י5Rµח†₪Ζ/◄1⌂¿•Ꜣ☀Z╤.☺⌐±⊗╦!═♯ß2Ԫ⌂ªEﺎY=§∅↔8♫0ӘФ☼\"Tσ½↕6CL±≥!^≠ﺎ{↓G=∇"
            "Y<~}Nѧ☼Ϟ۩ۈ↓☠٠Ѵ7÷U∩χΨ1ε3!↔ق4⊗+⊥£↕;=∗⇔1;2ע∴Κ@<α~Θ8<>\"8ִ5٨⊗⬤χ9↔ك↓Ωי◊↔"
            "◦Ω↔ש⇔Ω⊥↔Φφ۞↔";

        std::string output;
        uint64_t buffer = 0;  // Accumulated bits
        int bits_in_buffer = 0;

        for (char c : input) {
            size_t index = base512_chars.find(c);
            if (index == std::string::npos) {
                throw std::invalid_argument("Invalid character in Base512 input");
            }

            buffer = (buffer << 9) | index; // Add  9 bits
            bits_in_buffer += 9;

            while (bits_in_buffer >= 8) {
                output.push_back(static_cast<char>((buffer >> (bits_in_buffer - 8)) & 0xFF)); // Extract 8 bits
                bits_in_buffer -= 8;
            }
        }

        return output;
    };

    // Reverse Base512 to binary
    std::string bin_data = b12_reverse(b512_data);

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

PYBIND11_MODULE(hk512, m) {
    m.def("encode", &encode, "Encode a string in hk512");
    m.def("decode", &decode, "Decode an hk512 string");
}