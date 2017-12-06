# Makefile for code

PROGS = sum01
ASFLAGS = -g

all: $(PROGS)
# make knows how to compile .s files
$(PROGS):	% : %.o
	gcc -o $@ $<

clean:
	rm -vf *.o $(PROGS)
