#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <fstream>
#include <vector>
#include <optional>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;
namespace py = pybind11;

// Function to process a sound file (placeholder logic)
auto psound(const std::string& file) -> std::optional<std::string> {
    if (!fs::exists(file)) {
        return std::nullopt; // File doesn't exist
    }

    std::ifstream audioFile(file, std::ios::binary | std::ios::ate);
    if (!audioFile.is_open()) {
        return std::nullopt; // Failed to open the file
    }

    std::streamsize fileSize = audioFile.tellg();
    audioFile.seekg(0, std::ios::beg);

    std::vector<char> audioData(fileSize);
    if (!audioFile.read(audioData.data(), fileSize)) {
        return std::nullopt; // Failed to read the file
    }

    // Placeholder: Return a summary of the file
    return std::string("Sound file processed successfully!");
}

// Function to play a sound (placeholder logic)
void play(const std::string& file) {
    if (fs::exists(file)) {
        auto result = psound(file);
        if (result) {
            const std::string yellow = "\x1b[38;2;255;255;0m";
            const std::string red = "\x1b[38;2;255;0;0m";
            const std::string reset = "\x1b[0m";

            std::cout << yellow << "Playing sound: " << result.value() << reset << '\n';
        } else {
            std::cout << red << "Failed to process sound file." << reset << '\n';
        }
    } else {
        const std::string red = "\x1b[38;2;255;0;0m";
        const std::string reset = "\x1b[0m";
        std::cout << red << "File does not exist!" << reset << '\n';
    }
}

PYBIND11_MODULE(pytgm, m) {
    m.def("psound", &psound, "Process a sound file");
    m.def("play", &play, "Play a sound");
}