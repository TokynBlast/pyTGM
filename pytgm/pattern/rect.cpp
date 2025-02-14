#include <pybind11/pybind11.h>
#include <string>
#include <iostream>
#include <algorithm>

namespace py = pybind11;

void rect(int width, int height, int time=1, const char* char=" ") {
    int total_steps = (height * (height + 1)) / 2 + (height * (height - 1)) / 2 + (std::max(width - height, 0) * height);

    for (int i = 0; i < height; ++i) {
        line_length = std::min(++i, width);
        for (int j = 0; j < line_length; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (i-j+1) << "H" << char;
        }

    }
}

PYBIND11_MODULE(rect, m) {
    m.doc() = "Clears the screen, by printing out a specific char, to make a clearing animation";
    m.def("geky", &geky, "Prints out a rect of a specified size, in an animated form",
        py::arg("width"), py::arg("height"), py::arg("time")=1, py::arg("char")=" ");
}