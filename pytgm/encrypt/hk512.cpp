// Copyright TokynBlast
/*
HexKey-512 is an encryption designed for pyTGM.
It is NOT designed for super secure encryption needs.
*/

#include <pybind11/pybind11.h>
#include <random>
#include <string>
#include <bitset>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <numeric>

namespace py = pybind11;

std::mt19937 gen;

const std::string base512_chars =
    "░↕&∑~MCT#♦╕4(ρ@¾*>≠▀[{K+5♫£\\6]>7♪؛⅛9`%♠ڦO:3S♦]ژ♣╫⊕*O(◦G₸}◙↓±X╝9☻▒:"
    "↔▓]י5Rµח†₪Ζ/◄1⌂¿•Ꜣ☀Z╤.☺⌐±⊗╦!═♯ß2Ԫ⌂ªEﺎY=§∅↔8♫0ӘФ☼\"Tσ½↕6CL±≥!^≠ﺎ{↓G=∇"
    "Y<~}Nѧ☼Ϟ۩ۈ↓☠٠Ѵ7÷U∩χΨ1ε3!↔ق4⊗+⊥£↕;=∗⇔1;2ע∴Κ@<α~Θ8<>\"8ִ5٨⊗⬤χ9↔ك↓Ωי◊↔"
    "◦Ω↔ש⇔Ω⊥↔Φφ۞↔";

// **ENCODING FUNCTION**
std::string encode(const std::string& input, const std::string& key) {
    // Step 1: Shuffle input using the key
    std::vector<size_t> indices(input.size());
    std::iota(indices.begin(), indices.end(), 0);
    gen.seed(std::hash<std::string>{}(key));
    std::shuffle(indices.begin(), indices.end(), gen);

    std::string shuffled_input(input.size(), '\0');
    for (size_t i = 0; i < indices.size(); ++i) {
        shuffled_input[indices[i]] = input[i];
    }

    // Step 2: Apply key-based transformation (original addition method)
    std::string transformed_input = shuffled_input;
    for (size_t i = 0; i < transformed_input.length(); ++i) {
        transformed_input[i] = static_cast<char>(
            (static_cast<int>(transformed_input[i]) + static_cast<int>(key[i % key.length()])) % 256);
    }

    // Step 3: Convert to Base512
    std::string output;
    uint64_t buffer = 0;
    int bits_in_buffer = 0;

    for (unsigned char c : transformed_input) {
        buffer = (buffer << 8) | c;
        bits_in_buffer += 8;

        while (bits_in_buffer >= 9) {
            int index = (buffer >> (bits_in_buffer - 9)) & 0x1FF;
            output.push_back(base512_chars[index]);
            bits_in_buffer -= 9;
        }
    }

    if (bits_in_buffer > 0) {
        int index = (buffer << (9 - bits_in_buffer)) & 0x1FF;
        output.push_back(base512_chars[index]);
    }

    return output;
}

// **DECODING FUNCTION**
std::string decode(const std::string& data, const std::string& key) {
    // Step 1: Convert Base512 back to bytes
    std::string bin_data;
    uint64_t buffer = 0;
    int bits_in_buffer = 0;

    for (char c : data) {
        size_t index = base512_chars.find(c);
        if (index == std::string::npos) {
            throw std::invalid_argument("Invalid character in Base512 input");
        }

        buffer = (buffer << 9) | index;
        bits_in_buffer += 9;

        while (bits_in_buffer >= 8) {
            bin_data.push_back(static_cast<char>((buffer >> (bits_in_buffer - 8)) & 0xFF));
            bits_in_buffer -= 8;
        }
    }

    // Step 2: Reverse key-based transformation (original subtraction method)
    for (size_t i = 0; i < bin_data.length(); ++i) {
        bin_data[i] = static_cast<char>(
            (static_cast<int>(bin_data[i]) - static_cast<int>(key[i % key.length()]) + 256) % 256);
    }

    // Step 3: Reverse shuffle using the key
    std::vector<size_t> indices(bin_data.size());
    std::iota(indices.begin(), indices.end(), 0);
    gen.seed(std::hash<std::string>{}(key));
    std::shuffle(indices.begin(), indices.end(), gen);

    std::string original_data(bin_data.size(), '\0');
    for (size_t i = 0; i < indices.size(); ++i) {
        original_data[indices[i]] = bin_data[i];
    }

    return original_data;
}

// **PYBIND11 MODULE**
PYBIND11_MODULE(hk512, m) {
    m.doc() = "HexKey-512 Encoding/Decoding";
    m.def("encode", &encode, "Encode data with hk512", py::arg("data"), py::arg("key"));
    m.def("decode", &decode, "Decode an hk512 string", py::arg("data"), py::arg("key"));
}