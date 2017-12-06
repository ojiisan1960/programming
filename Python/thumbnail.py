#!/usr/bin/python

import os, sys
import Image

def createThumb(infile, maxwidth, maxheight):
    outfile = os.path.splitext(infile)[0] + ".thumb"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail((maxwidth,maxheight))
            im.save(outfile, "JPEG")
            return outfile
            
        except IOError:
            pass

    return ""

def thumbDir (path, maxwidth, maxheight):
    dirlist = os.listdir(path)
    dirlist.sort()
    piclist = []

    for i in range(len(dirlist)):
        foo = path + "/" + dirlist[i]
        ##print foo
        if os.path.isfile(foo):
            tname = createThumb(foo,maxwidth,maxheight)
            ##print "tname:",tname
            if tname != "":
                piclist.append((foo, tname))

    return piclist

def thumbHtml(piclist, rowsize):
    outfile = os.path.dirname(piclist[0][0]) + "/index.html"
    # print outfile

    f = open(outfile,'w')
    f.write('<html><body>\n')
    
    f.write('<table>\n')
    colcount = 0
    for i in range(len(piclist)):
        if colcount == 0:
            f.write('  <tr>\n')
        
        big = os.path.basename(piclist[i][0])
        little = os.path.basename(piclist[i][1])
        # print big, little
        f.write(' <td><table>\n')
        f.write('     <tr><td align=center valign=bottom><a href=' + big + '><img src=' + little + '></td></tr>\n')
        f.write('     <tr><td>' + big + '</td></tr>\n')
        f.write(' </table></td>\n')
        colcount = colcount + 1
        if colcount == rowsize:
            colcount = 0
            f.write('  </tr>\n')
    f.write('</table>\n')
    f.write('</body></html>\n')
    f.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        thumbHtml(thumbDir(sys.argv[1],64,64),8)
    
