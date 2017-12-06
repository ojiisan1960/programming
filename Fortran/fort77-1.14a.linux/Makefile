PREFIX=/usr
BINDIR=$(PREFIX)/bin
MANDIR=$(PREFIX)/man/man1
VERSION=1.14a

test:
	(cd tests; ./test.pl -v)

install: test
	install -m 755 fort77 $(BINDIR)
	install -m 644 fort77.1 $(MANDIR)

clean:
	rm -f *.bak *.o core */*.bak */*.o */core
dist:
	(cd ..; tar cf - fort77-$(VERSION) | gzip -9 > fort77-$(VERSION).tar.gz )
