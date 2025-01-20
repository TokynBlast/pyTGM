#include <iostream>
#include <conio.h>
#include <string>
#include <stdexcept>
#include <termios.h>
#include <unistd.h>

std::string geky(int times = 1) {
    try {
        for (int i = 0; i < times; ++i) {
            int k = _getch();
            if (k == 0 || k == 224) {
                k = _getch();
                if (k == 72) {
                    return "ArrowUp";
                } else if (k == 80) {
                    return "ArrowDown";
                } else if (k == 75) {
                    return "ArrowLeft";
                } else if (k == 77) {
                    return "ArrowRight";
                }
            } else {
                return std::string(1, static_cast<char>(k));
            }
        }
    } catch (...) {
        struct termios old, newt;
        tcgetattr(STDIN_FILENO, &old);
        newt = old;
        newt.c_lflag &= ~(ICANON | ECHO);
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);
        try {
            for (int i = 0; i < times; ++i) {
                char c;
                read(STDIN_FILENO, &c, 1);
                if (c == 27) {
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
                        } else {
                            return std::string(1, c) + std::string(seq, 2);
                        }
                    }
                } else {
                        return std::string(1, c);
                    }
                }
            }
        } finally {
            tcsetattr(STDIN_FILENO, TCSANOW, &old);
        }
    }
    return "";
}

