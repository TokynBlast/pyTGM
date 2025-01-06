// Copyright TokynBlast
#ifndef SKIP_PYTHON_H
#include <Python.h>
#endif

#include <filesystem>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <pybind11/pybind11.h>

namespace fs = std::filesystem;

auto fm_line(const std::string& file_loc, int line_number = 0, const std::string& pattern = "") -> int {
    if (!fs::exists(file_loc)) {
        std::cerr << "\033[31mError: \033[33mFile \"" << file_loc << "\" does not exist. Make sure it exists.\033[0m" << std::endl;
        return -1;
    }

    // Temporary file to store modified content
    std::string tempFilePath = file_loc + ".tmp";

    std::ifstream inputFile(file_loc);
    std::ofstream tempFile(tempFilePath);

    if (!inputFile.is_open() || !tempFile.is_open()) {
        std::cerr << "\033[31mError: \033[33mUnable to open the file.\033[0m" << std::endl;
        return -1;
    }

    std::string currentLine;
    int currentLineNumber = 0;
    bool modified = false;

    while (std::getline(inputFile, currentLine)) {
        if (currentLineNumber == line_number) {
            size_t pos = currentLine.find(pattern);
            if (pos != std::string::npos) {
                currentLine.replace(pos, pattern.length(), "<REPLACEMENT>"); // Example replacement
                modified = true;
            }
        }
        tempFile << currentLine << "\n";
        currentLineNumber++;
    }

    inputFile.close();
    tempFile.close();

    if (modified) {
        fs::rename(tempFilePath, file_loc);
        std::cout << "Line modified successfully.\n";
        return 0;
    } else {
        fs::remove(tempFilePath);
        std::cerr << "\033[31mError: \033[33mPattern not found or no modification needed.\033[0m" << std::endl;
        return -1;
    }
}

auto mod_line(const std::string& file, const std::string& txt, const int line, std::string p_hold = "") -> int {
    fm_line(file, line, txt)
    yellow = '\033[31m'
    red = '\033[33m'
    res = '\033[0m'
    std::cout << yellow << "WARNING: " << red << "mod_line() "
              << "will become fm_line in v4.2.0\n"
              << "You should begin using fm_line() as soon as possible." << endl;
}


PYBIND11_MODULE(file_modifier, m) -> void {
    m.doc() = "File modification utilities"; // Module docstring

    m.def("fm_line", &fm_line, py::arg("file_loc"), py::arg("line_number") = 0, py::arg("pattern") = "",
          "Modify a specific line in a file by replacing a pattern with '<REPLACEMENT>'.\n"
          "Args:\n"
          "    file_loc (str): The path to the file.\n"
          "    line_number (int): The line number to modify (default: 0).\n"
          "    pattern (str): The pattern to search for.\n"
          "Returns:\n"
          "    int: 0 if successful, -1 otherwise.");

    m.def("mod_line", &mod_line, py::arg("file"), py::arg("txt"), py::arg("line"), py::arg("p_hold") = "",
          "Deprecated: Use fm_line instead. Modify a line in a file and displays a warning.\n"
          "Args:\n"
          "    file (str): The path to the file.\n"
          "    txt (str): The text to search for.\n"
          "    line (int): The line number to modify.\n"
          "    p_hold (str): Placeholder for future arguments (default: '').\n"
          "Returns:\n"
          "    int: 0 if successful, -1 otherwise.");
}