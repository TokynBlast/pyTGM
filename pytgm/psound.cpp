#ifndef SKIP_PYTHON_H
#include <Python.h>
#endif

#include <iostream>
#include <string>

#include <pybind11/pybind11.h>

namespace fs = std::filesystem;
namespace py = pybind11;

void psound(const std::string& filename) {
    #if defined(_WIN32) || defined(_WIN64)
        #include <windows.h>
        #include <mmsystem.h>
        #pragma comment(lib, "winmm.lib")
        PlaySound(filename, NULL, SND_FILENAME | SND_ASYNC);
    
    #elif defined(__APPLE__)
        #include <AudioToolbox/AudioToolbox.h>
        CFStringRef cfString = CFStringCreateWithCString(NULL, filename, kCFStringEncodingUTF8);
        CFURLRef soundURL = CFURLCreateWithFileSystemPath(NULL, cfString, kCFURLPOSIXPathStyle, false);
        SystemSoundID soundID;
        AudioServicesCreateSystemSoundID(soundURL, &soundID);
        AudioServicesPlaySystemSound(soundID);
        CFRelease(soundURL);
        CFRelease(cfString);

    
    #elif defined(__linux__)
        #include <cstdlib>
        std::string command = "aplay -q ";
        command += filename;
        command += " &";
        std::system(command.c_str());
    #else
        std::cerr << "Sound playback not supported on this platform." << std::endl;
    #endif
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

auto PYBIND11_MODULE(sound_module, m) -> void {
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
