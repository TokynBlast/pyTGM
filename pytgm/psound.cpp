#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <fstream>
#include <vector>
#include <optional>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;
namespace py = pybind11;

// Function to validate and return audio file content
std::optional<std::vector<char>> psound(const std::string& file) {
    if (!fs::exists(file) || !fs::is_regular_file(file)) {
        return std::nullopt; // File doesn't exist or is not a regular file
    }

    std::ifstream audioFile(file, std::ios::binary | std::ios::ate);
    if (!audioFile.is_open()) {
        return std::nullopt; // Failed to open the file
    }

    std::streamsize fileSize = audioFile.tellg();
    if (fileSize <= 0) {
        return std::nullopt; // Empty file
    }

    audioFile.seekg(0, std::ios::beg);
    std::vector<char> audioData(static_cast<size_t>(fileSize));
    if (!audioFile.read(audioData.data(), fileSize)) {
        return std::nullopt; // Failed to read the file
    }

    return audioData; // Return the file content as a vector of bytes
}

// Function to print information about the audio file
void play(const std::string& file) {
    auto result = psound(file);
    if (result) {
        const auto& audioData = result.value();
        std::cout << "Playing sound with size: " << audioData.size() << " bytes\n";
    } else {
        std::cerr << "Error: Unable to play the sound file.\n";
    }
}

PYBIND11_MODULE(pytgm, m) {
    m.def("psound", &psound, "Process and validate a sound file");
    m.def("play", &play, "Play a sound file");
}