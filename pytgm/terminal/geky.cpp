#include <pybind11/pybind11.h>
#include <iostream>
#include <string>
#include <stdexcept>
#include <termios.h>
#include <unistd.h>


#ifdef _WIN32
#include <windows.h>
#else
#include <fcntl.h> // For non-blocking input
#endif

// Function to read a single character from standard input
char getch() {
#ifdef _WIN32
    // Windows-specific implementation
    HANDLE hStdin = GetStdHandle(STD_INPUT_HANDLE);
    DWORD mode;
    GetConsoleMode(hStdin, &mode);
    SetConsoleMode(hStdin, mode & ~ENABLE_LINE_INPUT & ~ENABLE_ECHO_INPUT);
    char c;
    ReadConsoleA(hStdin, &c, 1, nullptr, nullptr);
    SetConsoleMode(hStdin, mode);
    return c;
#else
    // Unix-like implementation
    struct termios old, newt;
    tcgetattr(STDIN_FILENO, &old);
    newt = old;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    char c;
    read(STDIN_FILENO, &c, 1);
    tcsetattr(STDIN_FILENO, TCSANOW, &old);
    return c;
#endif
}

std::string geky(int times = 1) {
    std::string result;
    struct termios old, newt;

    // Save the current terminal settings for cleanup
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
        // No known errors yet...
    }

    // Restore terminal settings
    tcsetattr(STDIN_FILENO, TCSANOW, &old);
    return result;
}

PYBIND11_MODULE(geky, m) {
    m.doc() = "Gets a single key input";
    m.def("geky", &geky, "Gets a single key input");
}