#include <pybind11/pybind11.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <chrono>

namespace py = pybind11;

void rect(int width, int height, int time=100, const char* character=" ") {
    int total_steps = (height * (height + 1)) / 2 + (height * (height - 1)) / 2 + (std::max(width - height, 0) * height);

    for (int i = 0; i < height; ++i) {
        int line_length = std::min(++i, width);
        for (int j = 0; j < line_length; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (i-j+1) << "H" << character;
            std::chrono::milliseconds ms(time);
        }

    }
}

PYBIND11_MODULE(rect, m) {
    m.doc() = "Clears the screen, by printing out a specific char, to make a clearing animation";
    m.def("rect", &rect, "Prints out a rect of a specified size, in an animated form",
        py::arg("width"), py::arg("height"), py::arg("time")=100, py::arg("character")=" ");
}