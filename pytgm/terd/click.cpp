// Copyright 2024 TokynBlast

#include <Python.h>
#include <tuple>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>     // For POSIX systems
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/input.h>
#include <cstdio>       // For perror
#endif

#include <pybind11/pybind11.h>

namespace py = pybind11;

// Function to detect click events
std::tuple<int, int> click() {
#ifdef _WIN32
    // Windows-specific implementation
    POINT cursorPos; // To store cursor position
    while (true) {
        if (GetAsyncKeyState(VK_LBUTTON) & 0x8000) { // Detect left mouse button press
            if (GetCursorPos(&cursorPos)) { // Retrieve cursor position
                return std::make_tuple(cursorPos.x, cursorPos.y); // Return position
            }
        }
        Sleep(10); // Avoid tight looping, give the CPU a break
    }
#else
    // POSIX implementation
    int fd = open("/dev/input/event0", O_RDONLY | O_NONBLOCK);
    if (fd < 0) {
        perror("Failed to open /dev/input/event0");
        return std::make_tuple(-1, -1);
    }

    struct input_event event;
    while (true) {
        ssize_t bytes = read(fd, &event, sizeof(event));
        if (bytes < 0) {
            if (errno != EAGAIN) {
                perror("Read error");
                break;
            }
            continue; // No data available, retry
        }

        if (bytes >= sizeof(event)) {
            if (event.type == EV_KEY && event.code == BTN_LEFT && event.value == 1) {
                close(fd);
                return std::make_tuple(event.type, event.code); // Detected left button press
            }
        }
    }

    close(fd);
    return std::make_tuple(-1, -1); // No click detected
#endif
}

// Pybind11 module definition
PYBIND11_MODULE(click, m) {
    m.doc() = "Pybind11 example plugin for detecting clicks";
    m.def("click", &click, "A function that detects mouse clicks and returns their type and code");
}
