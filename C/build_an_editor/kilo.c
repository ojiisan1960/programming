/*
 * This is an instruction booklet that shows you how to build a text editor in C.
 *
 * https://viewsourcecode.org/snaptoken/kilo/index.html
 *
 */

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>

struct termios orig_termios;

void disableRawMode() {
	tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig_termios);
	}

void enableRawMode() {
	tcgetattr(STDIN_FILENO, &orig_termios);
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

	tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw);
	}

/** MAIN **/

int main(){
	enableRawMode();

	while (1) {
	char c = '\0';
		read(STDIN_FILENO, &c, 1);
		if (iscntrl(c)) {
			printf("%d\r\n", c);
		} else {
			printf("%d ('%c')\r\n", c, c);
		}
		if ( c == 'q') break;
	}
	return 0;
	
	}

