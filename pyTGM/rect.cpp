#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <string>
#include <iostream>
#include <thread>
#include <chrono>

namespace nb = nanobind;

void rect(int width, int height, int time = 100, const std::string& character = " ") {
    int tot_steps = (height * (height + 1)) / 2 + (height * (height - 1)) / 2 + (std::max(width - height, 0) * height);
    int tot_time = time / tot_steps;

    for (int i = 0; i < height; ++i) {
        int line_length = std::min(i + 1, width);
        for (int j = 0; j < line_length; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (i - j + 1) << "H" << character;
            std::this_thread::sleep_for(std::chrono::milliseconds(tot_time));
        }
    }

    for (int i = height; i < width; ++i) {
        for (int j = 0; j < height; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (i - j + 1) << "H" << character;
            std::this_thread::sleep_for(std::chrono::milliseconds(tot_time));
        }
    }
    for (int i = 0; i < height; ++i) {
        for (int j = i; j < height; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (width - (j - i)) << "H" << character;
            std::this_thread::sleep_for(std::chrono::milliseconds(tot_time));
        }
    }

    std::cout << "\x1b[0;0H" << std::flush;
}

NB_MODULE(pyTGM, m) {
    m.def("rect", &rect, "Draw a rectangle animation",
          nb::arg("width"), nb::arg("height"), nb::arg("time") = 100, nb::arg("character") = " ");
}