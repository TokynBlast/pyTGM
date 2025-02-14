#include <pybind11/pybind11.h>
#include <iostream>
#include <string>
#include <stdexcept>

#ifdef _WIN32
#include <windows.h>
#include <conio.h>
#else
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
#endif

// Function to read a single character from standard input
char geky() {
#ifdef _WIN32
    return _getch(); // Windows implementation using conio.h
#else
    struct termios oldt, newt;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    char c;
    read(STDIN_FILENO, &c, 1);
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return c;
#endif
}

std::string geky(int times = 1) {
    std::string result;

#ifdef _WIN32
    for (int i = 0; i < times; ++i) {
        char c = getch();
        if (c == 0 || c == -32) { // Handle special keys in Windows
            c = getch();
            switch (c) {
                case 72: return "ArrowUp";
                case 80: return "ArrowDown";
                case 75: return "ArrowLeft";
                case 77: return "ArrowRight";
            }
        }
        return std::string(1, c);
    }
#else
    struct termios old, newt;
    if (!isatty(STDIN_FILENO)) {
        throw std::runtime_error("Standard input is not a terminal.");
    }
    tcgetattr(STDIN_FILENO, &old);
    newt = old;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    
    try {
        for (int i = 0; i < times; ++i) {
            char c = getch();
            if (c == 27) { // Handle arrow keys
                char seq[2];
                read(STDIN_FILENO, seq, 2);
                if (seq[0] == '[') {
                    switch (seq[1]) {
                        case 'A': return "ArrowUp";
                        case 'B': return "ArrowDown";
                        case 'C': return "ArrowRight";
                        case 'D': return "ArrowLeft";
                    }
                }
            } else {
                return std::string(1, c);
            }
        }
    } catch (...) {}
    
    tcsetattr(STDIN_FILENO, TCSANOW, &old);
#endif
    return result;
}

PYBIND11_MODULE(geky, m) {
    m.doc() = "Gets a single key input from the keyboard, a determinate number of times";
    m.def("geky", &geky, "Gets a single key input", pybind11::arg("times"));
}
