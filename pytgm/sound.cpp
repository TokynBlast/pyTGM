#ifdef _WIN32
    #include <windows.h>
    #include <mmsystem.h>
    #pragma comment(lib, "winmm.lib")
#endif

#ifdef _WIN64
    #include <windows.h>
    #include <mmsystem.h>
    #pragma comment(lib, "winmm.lib")
#endif

#ifdef __APPLE__
    #define __APPLE__
    #include <CoreFoundation/CoreFoundation.h>
    #include <AudioToolbox/AudioToolbox.h>
#endif

#ifdef __linux__
    #define linux_
    #include <cstdlib>
#endif

#ifndef CLANG_TIDY
#include <Python.h>
#endif

#include <iostream>
#include <string>

#include <pybind11/pybind11.h>

namespace fs = std::filesystem;
namespace py = pybind11;

void psound(const char* file) {
    #if defined(_WIN32) || defined(_WIN64)
        PlaySound(file, NULL, SND_FILENAME | SND_ASYNC);
    
    #elif defined(__APPLE__)
        CFStringRef cfString = CFStringCreateWithCString(NULL, filename, kCFStringEncodingUTF8);
        CFURLRef soundURL = CFURLCreateWithFileSystemPath(NULL, cfString, kCFURLPOSIXPathStyle, false);
        SystemSoundID soundID;
        AudioServicesCreateSystemSoundID(soundURL, &soundID);
        AudioServicesPlaySystemSound(soundID);
        CFRelease(soundURL);
        CFRelease(cfString);

    
    #elif defined(__linux__)
        std::string command = "aplay -q ";
        command += filename;
        command += " &";
        std::system(command.c_str());
    #else
        std::cerr << "Sound playback not supported on this platform." << std::endl;
    #endif
};

PYBIND11_MODULE(sound, m){
    m.doc() = "Sound playback and utility functions";  // Module docstring

    m.def("psound", &psound, py::arg("file"),
          "Play a sound file.\n"
          "Args:\n"
          "    file (str): Path to the sound file.\n"
          "Returns:\n"
          "    str: Optional error message, or None if successful.");
};
