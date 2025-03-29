//#pragma once

class Board {
	public:
//https://www.youtube.com/watch?v=VO6dSIvXlfM&list=PL2U2TQ__OrQ_TV2-wuHqGaK8qlnxgKUvK&index=2&ab_channel=CasualCoder
	int xMax, yMax;
	getmaxyx(stdscr, yMax, xMax);

	WINDOW *board_win = newwin(ROWS, COLS, (yMAX/2) - 10, (xMAX/2) - 10);
	box(board_win, 0, 0);
	wrefresh(board_win);


}
