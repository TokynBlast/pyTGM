// Copyright 2024 TokynBlast

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <filesystem>
#include <optional>
#include <cstdint>

namespace fs = std::filesystem;

std::optional<std::string> psound(const std::string& file) {
    if (fs::exists(file)) {
        std::ifstream audioFile(file, std::ios::binary | std::ios::ate);
        if (!audioFile.is_open()) {
            return "Error: Unable to open file.";
        }

        size_t fileSize = audioFile.tellg();
        audioFile.seekg(0, std::ios::beg);

        std::vector<char> audioData(fileSize);
        audioFile.read(audioData.data(), fileSize);

        // Windows
        #ifdef _WIN32
        HWAVEOUT hWaveOut;
        WAVEFORMATEX waveFormat;
        waveFormat.wFormatTag = WAVE_FORMAT_PCM;
        waveFormat.nChannels = 2;  // Stereo
        waveFormat.nSamplesPerSec = 44100;  // 44.1 kHz
        waveFormat.nAvgBytesPerSec = 44100 * 4;  // 16-bit stereo
        waveFormat.nBlockAlign = 4;
        waveFormat.wBitsPerSample = 16;
        waveFormat.cbSize = 0;

        waveOutOpen(&hWaveOut, WAVE_MAPPER, &waveFormat, 0, 0, CALLBACK_NULL);
        waveOutWrite(hWaveOut, reinterpret_cast<LPWAVEHDR>(audioData.data()), fileSize);
        waveOutClose(hWaveOut);

        // MacOS/Linux
        #elif __APPLE__ || __linux__
        int16_t* buffer = reinterpret_cast<int16_t*>(audioData.data());
        // Audio playback implementation for Linux/MacOS
        #endif

        return std::nullopt;  // Indicate success
    } else {
        return "Error: No file \"" + file + "\". Check if the file exists.";
    }
}

void play(const file) {
    if (fs::exist(file)) {
        psound(file)
    }

    const std::string yellow = '\x1b[38;2;255;255;0m';
    const std::string red = '\x1b[38;2;255;0;0m';
    const std::string reset = '\x1b[0m';

    std::cout << yellow << "WARNING: " << red << "sound.play() will become psound(str) in v4.2.1\n"
              << "After that, sound.play(str) will no longer be valid.\n"
              << "You should being using psound(str) now." << reset << endl;
    }

void generate(std::string p1 = "", std::string p2 = "", std::string p3 = "", 
              std::string p4 = "", std::string p5 = "") {
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



PYBIND11_MODULE(pytgm, m) {
    m.doc() = "C++ implementation of playing a sound from the terminal.";
    m.def("psound", &psound, "Plays a sound from the terminal.");
}
