/*
 * This is an instruction booklet that shows you how to build a text editor in C.
 *
 * https://viewsourcecode.org/snaptoken/kilo/index.html
 * Compeleted
 *  Chap 1: Setup
 *  Chap 2: Entering Raw Mode
 *
 */

/*** includes ***/
#include <errno.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <termios.h>

/*** Defines ***/
#define CTRL_KEY(k) ((k) & 0x1f)

/*** Data ***/
struct editorConfig {
	int screenrows;
	int screencols;
	struct termios orig_termios;
};

struct editorConfig E;

/*** Terminal ***/

void die(const char *s) {
	write(STDOUT_FILENO, "\x1b[2J", 4);
	write(STDOUT_FILENO, "\x1b[H", 3);

  	perror(s);
  	exit(1);
}

void disableRawMode() {
	if (tcsetattr(STDIN_FILENO, TCSAFLUSH, &E.orig_termios) == -1) die("tcsetattr");
}

void enableRawMode() {
	if (tcgetattr(STDIN_FILENO, &E.orig_termios) == -1) die("tcgetattr");
	atexit(disableRawMode);
	struct termios raw = E.orig_termios;
/* disable Ctrl-m, Ctrl-S and Ctrl-Q and misc*/
	raw.c_iflag &= ~( BRKINT | ICRNL | INPCK | ISTRIP | IXON);
/* disable newline and carriage return */
	raw.c_oflag &= ~( OPOST );
/* set character size to 8 bits */
	raw.c_cflag |= (CS8);
/* disable echo, cononical mode, Ctrl-v, Ctrl-c, Ctrl-z */
	raw.c_lflag &= ~(ECHO | ICANON | IEXTEN | ISIG);
/* read timeout */
	raw.c_cc[VMIN] = 0;
	raw.c_cc[VTIME] = 1;

	if (tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw) == -1) die("tcsetattr");
}

char editorReadKey() {
	int nread;
	char c;
	while ((nread = read(STDIN_FILENO, &c, 1)) != 1) {
	if (nread == -1 && errno != EAGAIN) die("read");
  }
	return c;
}

int getCursorPosition(int *rows, int *cols){
	if (write(STDOUT_FILENO, "\x1b[6n", 4) != 4) return -1;
	
	printf("\r\n");
	char c;
	while (read(STDIN_FILENO, &c, 1) == 1) {
		if (iscntrl(c)) {
			printf("%d\r\n", c);
		} else {
			printf("%d ('%c')\r\n", c, c);
			}
		}

	editorReadKey();
	return -1;
}

int getWindowSize(int *rows, int *cols){
	struct winsize ws;
	
	if ( 1 || ioctl(STDOUT_FILENO, TIOCGWINSZ, &ws) == -1 || ws.ws_col == 0){
		if (write(STDOUT_FILENO, "\x1b[999C\x1b[999B", 12) != 12) return -1;
		return getCursorPosition(rows, cols);
	} else {
		*cols = ws.ws_col;
		*rows = ws.ws_row;
		return 0;
	}
}

/******************************************************************************/
/*** Output ***/
/******************************************************************************/

void editorDrawRows(){
	int y;
	for (y = 0 ;y < E.screenrows; y++) {
		write(STDOUT_FILENO, "~\r\n", 3);
	}
}

void editorRefreshScreen(){
	write(STDOUT_FILENO, "\x1b[2J", 4);
	write(STDOUT_FILENO, "\x1b[H", 3);
	editorDrawRows();
	write(STDOUT_FILENO, "\x1b[H", 3);

		
}

/******************************************************************************/
/*** Input ***/
/******************************************************************************/

void editorProcessKeypress() {
	char c = editorReadKey();
  	switch (c) {
    case CTRL_KEY('q'):
	editorRefreshScreen();
/*		write(STDOUT_FILENO, "\x1b[2J", 4);
		write(STDOUT_FILENO, "\x1b[H", 3); 
*/
      exit(0);
      break;
  }
}

/*** Init ***/

void initEditor() {
	if (getWindowSize(&E.screenrows, &E.screencols) == -1) die("getWindowSize");
	}

int main(){
	enableRawMode();
	initEditor();

	while (1) {
	editorRefreshScreen();
	editorProcessKeypress();
	}

return 0;
	
}
