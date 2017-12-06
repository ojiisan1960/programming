/*
/ getname.c
/ Beginging Linux Programming 2nd Edition
/	page 503
*/

#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	char *host, **names, **addrs;
	struct hostent *hostinfo;
	
/* set host to argument supplied or use localhost */

	if(argc == 1) {
		char myname[256];
		gethostname(myname, 255);
		host = myname;
	}
	else
		host = argv[1];

/* Call gethostbyname and report an error if no information returned */
		
	hostinfo = gethostbyname(host);
	if(!hostinfo) {
		fprintf(stderr, "cannot get info for host: %s\n", host);
		exit(1);
	}

/* display the hostname and any aliases that it may have */
 
	printf("results for host %s:\n", host);
	printf("Name: %s\n", hostinfo -> h_name);
	printf("Aliases:");
	names = hostinfo -> h_aliases;
	while(*names) {
		printf(" %s", *names);
		names++;
	}
	printf("\n");
/* Warn and exit if the ehosts in question isn't and IP host */
 
	if(hostinfo -> h_addrtype != AF_INET) {
		fprintf(stderr, "not and IP host!\n");
		exit(1);
	}
	
/* Otherwise display the IP addresses */
	addrs = hostinfo -> h_addr_list;
	while(*addrs) {
		printf(" %s", inet_ntoa(*(struct in_addr *) *addrs ));
		addrs++;
	}
	printf("\n");
	exit(0);
}
