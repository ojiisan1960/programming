# Makefile for code

PROGS = prog6a prog6b prog6c prog6d

# if prog on cmd line
#ifneq ($(MAKECMDGOALS),)
#PROGS = $(MAKECMDGOALS)
#endif

all: $(PROGS)
# make knows how to compile .s files
$(PROGS):	% : %.o
	ld -o $@ $<

clean:
	rm -vf *.o $(PROGS)
