# Makefile for code

PROGS = prog10a 

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
