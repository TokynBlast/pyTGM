#include <ncurses.h>

initscr();
noecho();
cbreak();
keypad(stdscr, TRUE);

std::tuple<int, int> click() {
    MEVENT event;
    if (getmouse(&event) == OK) {
        return std::make_tuple(event.x, event.y);
    }
    endwin();
    return std::make_tuple(-1, -1);
}
