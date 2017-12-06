# Makefile for code

PROGS = prog15a  prog15b prog15c
ASFLAGS = -g
all: $(PROGS)
# make knows how to compile .s files
$(PROGS):	% : %.o
	ld -o $@ $<

clean:
	rm -vf *.o $(PROGS)
