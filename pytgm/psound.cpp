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

PYBIND11_MODULE(pytgm, m) {
    m.doc() = "C++ implementation of playing a sound from the terminal.";
    m.def("psound", &psound, "Plays a sound from the terminal.");
}
