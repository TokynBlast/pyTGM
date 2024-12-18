// Copyright 2024 TokynBlast

#include <Python.h>
#include <tuple>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/input.h>
#include <cstdio>
#endif

#include <pybind11/pybind11.h>

namespace py = pybind11;

// Function to detect click events
std::tuple<int, int> click() {
#ifdef _WIN32
    POINT cursorPos;
    while (true) {
        if (GetAsyncKeyState(VK_LBUTTON) & 0x8000) {
            if (GetCursorPos(&cursorPos)) {
                return std::make_tuple(cursorPos.x, cursorPos.y);
            }
        }
        Sleep(10);
    }
#else
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
            continue;
        }

        if (bytes >= sizeof(event)) {
            if (event.type == EV_KEY &&
                event.code == BTN_LEFT &&
                event.value == 1) {
                close(fd);
                return std::make_tuple(event.type, event.code);
            }
        }
    }

    close(fd);
    return std::make_tuple(-1, -1);
#endif
}

// Pybind11 module definition
PYBIND11_MODULE(click, m) {
    m.doc() = "Pybind11 example plugin for detecting clicks";
    m.def("click", &click, "Used to detect clicks within the terminal");
}
