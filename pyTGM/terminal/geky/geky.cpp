#include "geky.hpp"

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

std::string geky(int times = 1) {
    std::string result;

#ifdef _WIN32
    // Windows-specific key reading
    for (int i = 0; i < times; ++i) {
        char c = _getch();  // Read a single character
        if (c == 0 || c == -32) {  // Handle special keys
            c = _getch();  // Read the special key code
            switch (c) {
                case 72: result = "ArrowUp"; break;
                case 80: result = "ArrowDown"; break;
                case 75: result = "ArrowLeft"; break;
                case 77: result = "ArrowRight"; break;
            }
        } else {
            result = c;  // Regular character
        }
    }
#else
    // Unix-like (Linux/macOS) key reading
    for (int i = 0; i < times; ++i) {
        struct termios oldt, newt;
        tcgetattr(STDIN_FILENO, &oldt);
        newt = oldt;
        newt.c_lflag &= ~(ICANON | ECHO);  // Disable canonical mode and echo
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);
        char c;
        read(STDIN_FILENO, &c, 1);
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

        if (c == 27) {  // Handle escape sequence for arrow keys
            char seq[2];
            read(STDIN_FILENO, seq, 2);
            if (seq[0] == '[') {
                switch (seq[1]) {
                    case 'A': result = "ArrowUp"; break;
                    case 'B': result = "ArrowDown"; break;
                    case 'C': result = "ArrowRight"; break;
                    case 'D': result = "ArrowLeft"; break;
                }
            }
        } else {
            result += c;  // Regular character
        }
    }
#endif

    return result;
}
