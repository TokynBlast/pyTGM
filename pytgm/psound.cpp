// copyrigh 2024 TokynBlast
#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>
#include <optional>

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
        waveFormat.nChannels = 2; // Stereo
        waveFormat.nSamplesPerSec = 44100; // 44.1 kHz
        waveFormat.nAvgBytesPerSec = 44100 * 4; // 16-bit stereo
        waveFormat.nBlockAlign = 4;
        waveFormat.wBitsPerSample = 16;
        waveFormat.cbSize = 0;

        waveOutOpen(&hWaveOut, WAVE_MAPPER, &waveFormat, 0, 0, CALLBACK_NULL);
        waveOutWrite(hWaveOut, (LPWAVEHDR)audioData.data(), fileSize);
        waveOutClose(hWaveOut);

        // MacOS/Linux
        #elif __APPLE__
        AudioFileID audioFileID;
        ExtAudioFileOpenData* openData = &audioFileID;
        ExtAudioFileOpenURL(CFURLRef(), &audioFileID, 0);
        
        AudioStreamBasicDescription audioStreamFormat;
        UInt32 dataSize = sizeof(audioStreamFormat);
        ExtAudioFileGetProperty(audioFileID, kExtAudioFileProperty_FileDataFormat, &dataSize, &audioStreamFormat);

        UInt32 bufferSize = 1024;
        UInt32 numPacketsToRead = 256;
        UInt32 bufferByteSize = bufferSize * audioStreamFormat.mBytesPerFrame;

        UInt8* buffer = (UInt8*)malloc(bufferByteSize);
        UInt32 framesRead = 0;
        while (framesRead < numPacketsToRead) {
            UInt32 bytesRead = bufferByteSize;
            ExtAudioFileRead(audioFileID, &numPacketsToRead, &buffer);
            ExtAudioFileWrite(audioFileID, numPacketsToRead, buffer);
            framesRead += numPacketsToRead;
        }

        free(buffer);
        ExtAudioFileDispose(audioFileID);

        #elif __linux__
        snd_pcm_t *pcm_handle;
        snd_pcm_hw_params_t *params;
        int err;

        snd_pcm_open(&pcm_handle, "default", SND_PCM_STREAM_PLAYBACK, 0);
        snd_pcm_hw_params_malloc(&params);
        snd_pcm_hw_params_any(pcm_handle, params);
        snd_pcm_hw_params_set_access(pcm_handle, params, SND_PCM_ACCESS_RW_INTERLEAVED);
        snd_pcm_hw_params_set_format(pcm_handle, params, SND_PCM_FORMAT_S16_LE);
        snd_pcm_hw_params_set_rate_near(pcm_handle, params, &waveFormat.nSamplesPerSec, 0);
        snd_pcm_hw_params_set_channels(pcm_handle, params, waveFormat.nChannels);
        snd_pcm_hw_params(pcm_handle, params);
        snd_pcm_hw_params_free(params);

        short *buffer = (short*)audioData.data();
        snd_pcm_writei(pcm_handle, buffer, fileSize / 4);

        snd_pcm_close(pcm_handle);

        #endif

        return std::nullopt; // Indicate success
    } else {
        return "Error: No file \"" + file + "\". Check if the file exists.";
    }
}

PYBIND11_MODULE(pytgm, m) {
    m.doc() = "C++ implementation of playing a sound from the terminal.";
    m.def("psound", &psound, "Plays a sound from the terminal.");
}
