#include <iostream>
#include <string>
#include <stdexcept>
#include <termios.h>
#include <unistd.h>
#include <Python.h>
#include <pybind11/pybind11.h>

#ifdef _WIN32
#include <conio.h> // For _getch() on Windows
#else
#include <fcntl.h> // For non-blocking input
#endif

std::string geky(int times = 1) {
    struct termios old, newt;
    tcgetattr(STDIN_FILENO, &old);
    newt = old;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);

    std::string result;
    try {
        for (int i = 0; i < times; ++i) {
            char c;
#ifdef _WIN32
            c = _getch(); // Use _getch() on Windows
#else
            read(STDIN_FILENO, &c, 1); // Use read() on Unix-like systems
#endif
            if (c == 27) { // Escape character
                char seq[2];
                read(STDIN_FILENO, seq, 2);
                if (seq[0] == '[') {
                    if (seq[1] == 'A') {
                        return "ArrowUp";
                    } else if (seq[1] == 'B') {
                        return "ArrowDown";
                    } else if (seq[1] == 'C') {
                        return "ArrowRight";
                    } else if (seq[1] == 'D') {
                        return "ArrowLeft";
                    }
                }
            } else {
                return std::string(1, c);
            }
        }
    } catch (...) {
        // Handle any exceptions if necessary
    } finally {
        tcsetattr(STDIN_FILENO, TCSANOW, &old);
    }
    return result;
}

PYBIND11_MODULE(geky, m) {
    m.doc() = "Gets a single key input";
    m.def("geky", &geky, "Gets a single key input");
}