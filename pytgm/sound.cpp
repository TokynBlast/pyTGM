#include <pybind11/pybind11.h>
#include <string>

#ifdef _WIN32
    #define WIN
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

#include <iostream>
#include <string>

void sound(const char* filename) {
    #if defined(WIN)
        PlaySound(TEXT(filename), NULL, SND_FILENAME | SND_ASYNC);
    
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
    m.doc() = "Sound playback and utility functions";

    m.def("sound", &sound, pybind11::arg("filename"),
          "Play a sound file.\n"
          "Args:\n"
          "    file (str): Path to the sound file.\n"
          "Returns:\n"
          "    str: Error message, or None if successful.");
};
