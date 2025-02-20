#include <pybind11/pybind11.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

namespace py = pybind11;

class Table {
public:
    static std::string table_;

    static std::string gen(const std::string& chars = table_, int times = 1) {
        std::string b64table = chars.empty() ? table_ : chars;
        std::vector<char> b64list(b64table.begin(), b64table.end());
        for (int i = 0; i < times; ++i) {
            std::random_shuffle(b64list.begin(), b64list.end());
        }
        return std::string(b64list.begin(), b64list.end());
    }

    static void reset() {
        table_ = "ABCDEFGHIJKL "
                 "MNOPQRSTUVWXYZabcdefghijk "
                 "lmnopqrstuvwxyz1234567890?!@#$%^& "
                 "*()_+-=[]{}\\|/,.<>~`;:'\" ";
    }
};

std::string Table::table_ = "ABCDEFGHIJKL "
                             "MNOPQRSTUVWXYZabcdefghijk "
                             "lmnopqrstuvwxyz1234567890?!@#$%^& "
                             "*()_+-=[]{}\\|/,.<>~`;:'\" ";

std::string encode(const std::string& text) {
    std::string bins;
    for (char c : text) {
        bins += std::bitset<8>(static_cast<unsigned char>(c)).to_string();
    }
    while (bins.length() % 6 != 0) {
        bins += '0';
    }
    std::vector<std::string> binChunks;
    for (size_t i = 0; i < bins.length(); i += 6) {
        binChunks.push_back(bins.substr(i, 6));
    }

    std::string base64;
    for (const std::string& b : binChunks) {
        if (b == "000000") {
            base64 += '=';
        } else {
            base64 += Table::table_[std::stoi(b, nullptr, 2)];
        }
    }
    return base64;
}

std::string decode(const std::string& text) {
    std::string bins;
    for (char c : text) {
        if (c == '=') {
            bins += "000000";
        } else {
            bins += std::bitset<6>(Table::table_.find(c)).to_string();
        }
    }
    std::vector<std::string> binChunks;
    for (size_t i = 0; i < bins.length(); i += 8) {
        binChunks.push_back(bins.substr(i, 8));
    }

    std::string decoded_text;
    for (const std::string& b : binChunks) {
        if (b != "00000000") {
            decoded_text += static_cast<char>(std::stoi(b, nullptr, 2));
        }
    }
    return decoded_text;
}

PYBIND11_MODULE(base64_module, m) {
    py::class_<Table>(m, "Table")
        .def_static("gen", &Table::gen)
        .def_static("reset", &Table::reset);

    m.def("encode", &encode);
    m.def("decode", &decode);
}

