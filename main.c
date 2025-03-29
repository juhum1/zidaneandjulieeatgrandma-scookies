#include <ncurses.h>
#include "board.c"
#include "enemies.h"
#include "gamefunctions.h"
#include "towers.h"

#define ROWS 20
#define COLS 20

int main()
{	
	initscr();
	refresh();
	
	struct Status status = {100, 100, 0, 0};
	struct Enemy enemies [100];
	struct Tower towers [5];

	

	getch();
	endwin();

	return 0;
}
