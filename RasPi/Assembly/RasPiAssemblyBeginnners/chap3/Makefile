# Makefile for code

PROGS = prog3a prog3a_hex prog3a_bin

# if prog on cmd line
#ifneq ($(MAKECMDGOALS),)
#PROGS = $(MAKECMDGOALS)
#endif

all: $(PROGS)
# make knows how to compile .s files
$(PROGS):	% : %.o
	ld -o $@ $<

allparts:
	ld -o allparts part1.o part2.o
part1:	
	 as -o part1.o part1.s
part2:
	 as -o part2.o part2.s

clean:
	rm -vf *.o $(PROGS)
