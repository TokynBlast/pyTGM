#include "rect.hpp"
#include <nanobind/nanobind.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <chrono>

void rect(int width, int height, int time=100, const char* character=" ") {
    int tot_steps = (height * (height + 1)) / 2 + (height * (height - 1)) / 2 + (std::max(width - height, 0) * height);
    int tot_time = time / tot_steps;

    for (int i = 0; i < height; ++i) {
        int line_length = std::min(++i, width);
        for (int j = 0; j < line_length; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (i-j+1) << "H" << character;
            std::chrono::milliseconds ms(tot_time);
        }
    }

    for (int i = height; i < width; ++i) {
        for (int j = 0; j < height; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (i-j+1) << "H" << character;
            std::chrono::milliseconds ms(tot_time);
        }
    }

    for (int i = 0; i < height; ++i) {
        for (int j = i; j < height; ++j) {
            std::cout << "\x1b[" << (j + 1) << ";" << (width - (j - i)) << "H" << character;
        }
    }
}