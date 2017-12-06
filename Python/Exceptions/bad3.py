MyError = "My error"

def stuff(file):
    raise MyError

file = open('data', 'r')    #open an existing file
try:
    stuff(file)		    # raises an exception
finally:
    file.close()	    # always close file
