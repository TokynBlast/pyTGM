#include <iostream>
#include <pybind11/pybind11.h>

int cls() {
    #ifdef _WIN32
        #include <windows.h>
        HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
        CONSOLE_SCREEN_BUFFER_INFO csbi;
        DWORD written;
        COORD topLeft = {0, 0};

        if (GetConsoleScreenBufferInfo(hConsole, &csbi)) {
            DWORD consoleSize = csbi.dwSize.X * csbi.dwSize.Y;
            FillConsoleOutputCharacter(hConsole, ' ', consoleSize, topLeft, &written);
            FillConsoleOutputAttribute(hConsole, csbi.wAttributes, consoleSize, topLeft, &written);
            SetConsoleCursorPosition(hConsole, topLeft);
        }

    #else
        std::cout << "\033[H\033[J";
    #endif

    return 0;
}

PYBIND11_MODULE(cls, m) {
    m.doc() = "Clears the screen";
    m.def("cls", &cls, "Clears the terminal screen");
}