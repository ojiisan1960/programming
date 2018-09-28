/*
 * This is an instruction booklet that shows you how to build a text editor in C.
 *
 * https://viewsourcecode.org/snaptoken/kilo/index.html
 * Completed
 *  Chap 1: Setup
 *  Chap 2: Entering Raw Mode
 * 	Chap 3: rawInputAndOutput ( fail to build at Step 26 )
 */

/*** includes ***/
#include <errno.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>

/** DEFINES ***/

#define CTRL_KEY(k) ((k) & 0x1f)

/*** DATA ***/

struct termios orig_termios;


/*** TERMINAL ***/

void die(const char *s) {
  write(STDOUT_FILENO, "\x1b[2J", 4);
  write(STDOUT_FILENO, "\x1b[H", 3);
  perror(s);
  exit(1);
}

void disableRawMode() {
	if (tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig_termios) == -1) 
	die("tcsetattr");
}

void enableRawMode() {
	if (tcsetattr(STDIN_FILENO, &orig_termios) == -1) 
	die("tcgetattr");
	atexit(disableRawMode);

	struct termios raw = orig_termios;
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

	if (tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw) == -1) 
	die("tcsetattr");
}

char editorReadKey() {
  int nread;
  char c;
  while ((nread = read(STDIN_FILENO, &c, 1)) != 1) {
    if (nread == -1 && errno != EAGAIN) die("read");
  }
  return c;
}

/*** OUTPUT ***/

void editorDrawRows() {
  int y;
  for (y = 0; y < 24; y++) {
    write(STDOUT_FILENO, "~\r\n", 3);
  }
}

void editorRefreshScreen() {
/* clear the screen and position the cursor */
  write(STDOUT_FILENO, "\x1b[2J", 4);
  write(STDOUT_FILENO, "\x1b[H", 3);
  editorDrawRows();
  write(STDOUT_FILENO, "\x1b[H", 3);
}

/*** INPUT ***/

void editorProcessKeypress() {
  char c = editorReadKey();
  switch (c) {
    case CTRL_KEY('q'):
  		write(STDOUT_FILENO, "\x1b[2J", 4);
  		write(STDOUT_FILENO, "\x1b[H", 3);
      exit(0);
      break;
  }
}
/*** MAIN ***/

int main(){
	enableRawMode();

	while (1) {
		editorRefreshScreen();
		editorProcessKeypress();
	}
	return 0;
	
}
