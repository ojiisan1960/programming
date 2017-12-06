def kaboom(list, n):
    print list[n]	# Trigger index error

try:
    kaboom([0, 1, 2], 3)
except IndexError:	    #catch exception here
    print "Hello world!"
