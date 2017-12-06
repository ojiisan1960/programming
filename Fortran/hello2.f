C This is a Comment Line.
PROGRAM HELLO
C This program greets the user.
CHARACTER NAME *8
C NAME is an 8 character string.
PRINT*, ’Please type in your name:’
READ*, NAME
C Read an 8 character string.
PRINT 5, NAME
5 FORMAT(’Hello’, A)
C Print two strings.
END
