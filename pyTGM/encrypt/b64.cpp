#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <stdexcept>
#include <bitset>

class Table {
public:
    // Default base64 table (using a raw string literal to avoid excessive escaping)
    static std::string table_;

    // Generates a new table by shuffling the provided table (or the default if empty)
    static std::string gen(const std::string &chars="", int times = 1) {
        std::string b64table = chars.empty() ? table_ : chars;
        std::vector<char> b64list(b64table.begin(), b64table.end());
        std::random_device rd;
        std::mt19937 g(rd());
        for (int i = 0; i < times; i++) {
            std::shuffle(b64list.begin(), b64list.end(), g);
        }
        return std::string(b64list.begin(), b64list.end());
    }

    // Resets the table to the default value.
    static void reset() {
        table_ = R"(ABCDEFGHIJKL MNOPQRSTUVWXYZabcdefghijk lmnopqrstuvwxyz1234567890?!@#$%^& *()_+-=[]{}\|/,.<>~`;:'")";
    }
};

// Initialize the static table_ member with the default value.
std::string Table::table_ = R"(ABCDEFGHIJKL MNOPQRSTUVWXYZabcdefghijk lmnopqrstuvwxyz1234567890?!@#$%^& *()_+-=[]{}\|/,.<>~`;:'")";

// Encodes input text into a custom base64 string using Table::table_.
std::string encode(const std::string &text) {
    std::string bins;
    // Convert each character to its 8-bit binary representation.
    for (char c : text) {
        bins += std::bitset<8>(static_cast<unsigned char>(c)).to_string();
    }
    // Pad the binary string until its length is divisible by 6.
    while (bins.size() % 6 != 0) {
        bins.push_back('0');
    }

    std::string base64;
    // Process every 6-bit chunk.
    for (size_t i = 0; i < bins.size(); i += 6) {
        std::string chunk = bins.substr(i, 6);
        if (chunk == "000000") {
            base64.push_back('=');
        } else {
            unsigned long index = std::bitset<6>(chunk).to_ulong();
            if (index >= Table::table_.size()) {
                throw std::out_of_range("Index out of range in Table::table_");
            }
            base64.push_back(Table::table_[index]);
        }
    }
    return base64;
}

// Decodes text encoded with the custom base64 scheme using Table::table_.
std::string decode(const std::string &text) {
    std::string bins;
    // For each character in the input, convert it back to a 6-bit binary string.
    for (char c : text) {
        if (c == '=') {
            bins += "000000";
        } else {
            size_t pos = Table::table_.find(c);
            if (pos == std::string::npos) {
                throw std::invalid_argument("Character not found in base64 table");
            }
            bins += std::bitset<6>(static_cast<unsigned long>(pos)).to_string();
        }
    }

    std::string decoded;
    // Process every 8-bit chunk.
    for (size_t i = 0; i < bins.size(); i += 8) {
        std::string byteStr = bins.substr(i, 8);
        // Skip chunks that are exactly "00000000"
        if (byteStr == "00000000") continue;
        int value = std::stoi(byteStr, nullptr, 2);
        decoded.push_back(static_cast<char>(value));
    }
    return decoded;
}

PYBIND11_MODULE(b64, m) {
    m.doc() = "This module is used for encoding and decoding in base64. A custom table can also be set.";

    pybind11::class_<Table>(m, "Table")
        .def_static("gen", &Table::gen,
                   pybind11::arg("chars") = "",
                   pybind11::arg("times") = 1,
                   "Generates a new table by shuffling the given table or the default table.")
        .def_static("reset", &Table::reset,
                   "Resets the table to the default value.");

    m.def("encode", &encode, pybind11::arg("text"),
          "Encodes inputted data in base64, using the table variable.");
    m.def("decode", &decode, pybind11::arg("text"),
          "Decodes encoded data in base64, using the table variable.");
}
