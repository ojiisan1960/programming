import re, os, sys, time

pat = r"""(?x)                          # enable long format
        (\S+\s+\S+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+ # date
        (\d+)\s+                        # number
        (\S+)\s+                        # host
        (\d+)\s+                        # bytes
        (\S+)\s+                        # file
        """

def report(n, t0, nh):
    print "%7d good lines in %.3f seconds" % (n, time.clock() - t0),
    print "(%d unique hosts)" % nh

def main():
    t0 = time.clock()
    prog = re.compile(pat)
    if sys.argv[1:]:
        file = sys.argv[1]
    else:
        file = "xferlog-2001-02"
    f = open(file)
    n = 0
    table = {}
    hosts = {}
    for line in f.xreadlines():
        m = prog.match(line)
        if not m:
            print "bad line", `line`
        else:
            n = n+1
            url = m.group(5)
            table[url] = table.get(url, 0) + 1
            host = m.group(3)
            hosts[host] = hosts.get(host, 0) + 1
            if n%50000 == 0:
                report(n, t0, len(hosts))
    report(n, t0, len(hosts))
    list = [(count, url) for url, count in table.items()]
    list.sort()
    list.reverse()
    for count, url in list[:100]:
        print "%7d %s" % (count, url)

main()