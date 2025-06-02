#include <nanobind/nanobind.h>

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
    #include <alsa/asoundlib.h>
    #include <fstream>
    #include <vector>
#endif

#include <iostream>
#include <string>

int sound(const char* filename) {
    #if defined(WIN)
        PlaySoundA(filename, NULL, SND_FILENAME | SND_ASYNC);

    #elif defined(__APPLE__)
        CFStringRef cfString = CFStringCreateWithCString(NULL, filename, kCFStringEncodingUTF8);
        CFURLRef soundURL = CFURLCreateWithFileSystemPath(NULL, cfString, kCFURLPOSIXPathStyle, false);
        SystemSoundID soundID;
        AudioServicesCreateSystemSoundID(soundURL, &soundID);
        AudioServicesPlaySystemSound(soundID);
        CFRelease(soundURL);
        CFRelease(cfString);

    #elif defined(__linux__)
        snd_pcm_t* handle;
        snd_pcm_hw_params_t* params;
        unsigned int rate = 44100;
        int channels = 2;
        snd_pcm_uframes_t frames = 32;

        if (snd_pcm_open(&handle, "default", SND_PCM_STREAM_PLAYBACK, 0) < 0) {
            std::cerr << "Error opening PCM device." << std::endl;
            return 1;
        }

        snd_pcm_hw_params_malloc(&params);
        snd_pcm_hw_params_any(handle, params);
        snd_pcm_hw_params_set_access(handle, params, SND_PCM_ACCESS_RW_INTERLEAVED);
        snd_pcm_hw_params_set_format(handle, params, SND_PCM_FORMAT_S16_LE);
        snd_pcm_hw_params_set_channels(handle, params, channels);
        snd_pcm_hw_params_set_rate_near(handle, params, &rate, nullptr);
        snd_pcm_hw_params_set_period_size_near(handle, params, &frames, nullptr);
        snd_pcm_hw_params(handle, params);
        snd_pcm_hw_params_free(params);

        std::ifstream file(filename, std::ios::binary);
        if (!file) {
            std::cerr << "Could not open file.\n";
            return 1;
        }

        file.seekg(44); // Skip WAV header
        std::vector<char> buffer(4096);
        while (!file.eof()) {
            file.read(buffer.data(), buffer.size());
            auto size = file.gcount();
            if (size > 0)
                snd_pcm_writei(handle, buffer.data(), size / 4); // 16-bit stereo
        }

        snd_pcm_drain(handle);
        snd_pcm_close(handle);

    #else
        std::cerr << "Sound playback not supported on this platform." << std::endl;
        return 1;
    #endif

    return 0;
}

namespace nb = nanobind;
using namespace nb::literals;

NB_MODULE(pyTGM, m) {
    m.def("sound", &sound, "filename"_a, "Play a WAV sound file.");
}
