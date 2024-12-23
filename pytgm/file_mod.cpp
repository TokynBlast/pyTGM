#include <pybind11/pybind11.h>
#include <fstream>
#include <string>
#include <optional>

namespace py = pybind11;

// Struct to encapsulate parameters for fm_line to avoid easily swappable parameters
struct FindLineParams {
    std::string file_loc;
    int line_number = 0;
    std::string pattern = "";
};

// Function to find a line in a file
auto fm_line(const FindLineParams& params) -> int {
    std::ifstream file(params.file_loc);
    if (!file.is_open()) {
        return -1; // File not found or cannot be opened
    }

    std::string line;
    int current_line = 0;
    while (std::getline(file, line)) {
        ++current_line;
        if (!params.pattern.empty() && line.find(params.pattern) != std::string::npos) {
            return current_line;
        }
        if (current_line == params.line_number) {
            return current_line;
        }
    }
    return -1; // Line not found
}

// Function to modify a line in a file
auto mod_line(const std::string& file, const std::string& txt, int line, const std::string& p_hold = "") -> int {
    std::ifstream in_file(file);
    if (!in_file.is_open()) {
        return -1; // File not found or cannot be opened
    }

    const std::string temp_file = file + ".tmp";
    std::ofstream out_file(temp_file);
    if (!out_file.is_open()) {
        return -1; // Temporary file could not be created
    }

    std::string line_data;
    int current_line = 0;
    bool modified = false;

    while (std::getline(in_file, line_data)) {
        ++current_line;
        if ((current_line == line || (!p_hold.empty() && line_data.find(p_hold) != std::string::npos)) && !modified) {
            out_file << txt << '\n';
            modified = true;
        } else {
            out_file << line_data << '\n';
        }
    }

    in_file.close();
    out_file.close();

    if (modified) {
        if (std::remove(file.c_str()) != 0 || std::rename(temp_file.c_str(), file.c_str()) != 0) {
            return -1; // Error renaming the file
        }
    } else {
        std::remove(temp_file.c_str());
    }

    return modified ? 0 : -1;
}

PYBIND11_MODULE(pytgm, m) {
    m.def("fm_line", &fm_line, "Find a line in a file");
    m.def("mod_line", &mod_line, "Modify a line in a file");
}