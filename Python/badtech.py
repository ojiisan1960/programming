#!/usr/bin/python
""" badtech.py - simple script for retrieving the latest badtech
    comic strip.
    It can be set up as a cron job, useful for those archiving
    their comic strips. You might want to set the path to where
    the image gets stored.
"""

__author__ = 'Dietmar Lang <dietmar@wh.fh-wedel.de>'
__date__ = '2001/09/09'


import urllib, string, time

def filename():
    """Formats a filename based on the date. A matter of taste.
    Example for September 2nd, 2001 it will be '2001-09September-02.jpg'"""
    
    monthnames = {'1':'January', '2':'February', '3':'March', '4':'April',
                  '5':'May', '6':'June', '7':'July', '8':'August','9':'September',
                  '10':'October', '11':'November', '12':'December'}    
    name = year_long+'-'+string.zfill(month, 2)+monthnames[month]+'-' \
           +string.zfill(day, 2)+'.jpg'
    return name

# get the current date
timetuple = time.localtime(time.time())
day = `timetuple[2]`
month = `timetuple[1]`
year_long = `timetuple[0]`
year = year_long[-1:]
  
url = 'http://www.badtech.com/a/'+year+'/'+month+'/'+day+'.jpg'

print 'Retrieving Badtech comic strip...',
try:
    image = urllib.URLopener()
    image.retrieve(url, filename())
except:
    print 'Error during retrieval! Maybe Badtech is no more? ;)'
else:
    print 'done.'
