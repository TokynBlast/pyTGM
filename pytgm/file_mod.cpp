// Copyright TokynBlast
#include <filesystem>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <pybind11/pybind11.h>

namespace fs = std::filesystem;

int fm_line(const std::string& file_loc, int line_number = 0, const std::string& pattern = "") {
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

int mod_line(const std::string& file, const std::string& txt, const int line, std::string p_hold = "") {
    fm_line(file, line, txt)
    yellow = '\033[31m'
    red = '\033[33m'
    res = '\033[0m'
    std::cout << yellow << "WARNING: " << red << "mod_line() "
              << "will become fm_line in v4.2.0\n"
              << "You should begin using fm_line() as soon as possible." << endl;
}


PYBIND11_MODULE(pytgm, m) {
    m.doc() = "A more complex way for I/O with files";
    m.def("fm_line", &fm_line, "Modify a single line of a file");
}