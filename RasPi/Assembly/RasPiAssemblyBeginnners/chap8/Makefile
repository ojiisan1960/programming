# Makefile for code

PROGS = prog8a prog8b toggle_case upper_to_lower

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
