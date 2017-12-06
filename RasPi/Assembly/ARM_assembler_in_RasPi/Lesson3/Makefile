# Makefile for code

PROGS = load01 store01
# add debugging
ASFLAGS = -g

all: $(PROGS)
# make knows how to compile .s files
$(PROGS):	% : %.o
	gcc -o $@ $<

clean:
	rm -vf *.o $(PROGS)
