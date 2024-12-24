#include <optional>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>
#include <pybind11/pybind11.h>

namespace fs = std::filesystem;
namespace py = pybind11;

auto psound(const std::string& file) -> std::optional<std::string> {
    std::ifstream audioFile(file, std::ios::binary);
    if (!audioFile) {
        return "Failed to open file";
    }

    audioFile.seekg(0, std::ios::end);
    auto fileSize = static_cast<std::streamsize>(audioFile.tellg());
    audioFile.seekg(0, std::ios::beg);

    std::vector<char> audioData(fileSize);
    audioFile.read(audioData.data(), fileSize);

    if (!audioFile) {
        return "Failed to read file";
    }

    // Process audioData...
    return std::nullopt;
}

void play(const std::string& file) {
    if (fs::exists(file)) {
        psound(file);
    } else {
        std::cerr << "File does not exist: " << file << std::endl;
    }
}

void generate(const std::string& p1 = "", const std::string& p2 = "", const std::string& p3 = "", const std::string& p4 = "", const std::string& p5 = "") {
    (void)p1;
    (void)p2;
    (void)p3;
    (void)p4;
    (void)p5;

    const std::string yellow = "\033[38;2;255;255;0m";
    const std::string red = "\033[38;2;255;0;0m";
    const std::string reset = "\033[0m";

    std::cout << yellow << "WARNING: " << red 
              << "sound.generate() is no longer implemented\n"
              << "This change was made in 4.1.0, this function will be removed entirely in 4.2.0\n"
              << "If you want to play a sound, use psound(std::string file_path)" 
              << reset << std::endl;
}

PYBIND11_MODULE(sound_module, m) {
    m.doc() = "Sound playback and utility functions";  // Module docstring

    m.def("psound", &psound, py::arg("file"),
          "Play a sound file.\n"
          "Args:\n"
          "    file (str): Path to the sound file.\n"
          "Returns:\n"
          "    str: Optional error message, or None if successful.");

    m.def("play", &play, py::arg("file"),
          "Deprecated: Use psound instead. Play a sound file and display a warning.\n"
          "Args:\n"
          "    file (str): Path to the sound file.");

    m.def("generate", &generate, py::arg("p1") = "", py::arg("p2") = "", py::arg("p3") = "",
          py::arg("p4") = "", py::arg("p5") = "",
          "Deprecated: Dummy function. Displays a warning that it is no longer implemented.");
}