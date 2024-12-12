#include <ncurses.h>
#include <tuple>

std::tuple<int, int> getMouseClick() {
    initscr();
    noecho();
    cbreak();
    keypad(stdscr, TRUE);

    MEVENT event;

    if (getmouse(&event) == OK) {
        endwin();
        return std::make_tuple(event.x, event.y);
    }

    endwin();
    return std::make_tuple(-1, -1);
}