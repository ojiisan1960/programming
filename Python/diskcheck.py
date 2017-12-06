#!/usr/bin/python
#
# DiskCheck program 1.0
# Copyright (c) 2001 Red Hat, Inc. All rights reserved.
#
# This software may be freely redistributed under the terms of the GNU
# public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 675 Mass Ave, Cambmridge, MA 02139, USA.
#
# Author: Preston Brown <pbrown@redhat.com>
# Fixes by Aleksey Nogin <ayn2@cornell.edu>
#
# Inspiration for this program comes from a perl script of the same name
# by Kirk Bauer <kirk@kaybee.org> and Benjamin Cabell <q98@beseix.org>

FileMissing     = 'Conf.FileMissing'
IndexError      = 'Conf.IndexError'
BadFile         = 'Conf.BadFile'
WrongMethod     = 'Conf.WrongMethod'
VersionMismatch = 'Conf.VersionMismatch'
SystemFull      = 'conf.SystemFull'

from string import *
import regex
import re
import string
import regsub
import os

# Implementation:
# A configuration file is a list of lines.
# a line is a string.

class Conf:
    def __init__(self, filename, commenttype='#',
                 separators='\t ', separator='\t',
		 merge=1, create_if_missing=1):
        self.commenttype = commenttype
        self.separators = separators
        self.separator = separator
	self.merge = merge
	self.create_if_missing = create_if_missing
        self.line = 0
	self.rcs = 0
        self.mode = -1
        # self.line is a "point" -- 0 is before the first line;
        # 1 is between the first and second lines, etc.
        # The "current" line is the line after the point.
        self.filename = filename
        self.read()
    def rewind(self):
        self.line = 0
    def fsf(self):
        self.line = len(self.lines)
    def tell(self):
        return self.line
    def seek(self, line):
        self.line = line
    def nextline(self):
        self.line = min([self.line + 1, len(self.lines)])
    def findnextline(self, regexp='.*'):
        # returns false if no more lines matching pattern
        while self.line < len(self.lines):
            if re.search(regexp, self.lines[self.line]):
                return 1
            self.line = self.line + 1
        # if while loop terminated, pattern not found.
        return 0
    def findnextcodeline(self):
        # optional whitespace followed by non-comment character
        # defines a codeline.  blank lines, lines with only whitespace,
        # and comment lines do not count.
        return self.findnextline('^[' + self.separators + ']*' +
                             '[^' + self.commenttype + self.separators + ']+')
    def findlinewithfield(self, fieldnum, value):
	if self.merge:
	    seps = '['+self.separators+']+'
	else:
	    seps = '['+self.separators+']'
	rx = '^'
	for i in range(fieldnum - 1):
	    rx = rx + '[^'+self.separators+']*' + seps
	rx = rx + value + '\(['+self.separators+']\|$\)'
	return self.findnextline(rx)
    def getline(self):
        if self.line >= len(self.lines):
            return ''
        return self.lines[self.line]
    def getfields(self):
        # returns list of fields split by self.separators
        if self.line >= len(self.lines):
            return []
	if self.merge:
	    seps = '['+self.separators+']+'
	else:
	    seps = '['+self.separators+']'
        #print "regsub.split(self.lines[%s], %s) = %s" % (self.line, seps, regsub.split(self.lines[self.line], seps))
        return regsub.split(self.lines[self.line], seps)
    def setfields(self, list):
	# replaces current line with line built from list
	# appends if off the end of the array
	if self.line < len(self.lines):
	    self.deleteline()
	self.insertlinelist(list)
    def insertline(self, line=''):
        self.lines.insert(self.line, line)
    def insertlinelist(self, linelist):
        self.insertline(joinfields(linelist, self.separator))
    def sedline(self, pat, repl):
        if self.line < len(self.lines):
            self.lines[self.line] = regsub.gsub(pat, repl, \
                                                self.lines[self.line])
    def changefield(self, fieldno, fieldtext):
        fields = self.getfields()
        fields[fieldno:fieldno+1] = [fieldtext]
        self.setfields(fields)
    def setline(self, line=[]):
        self.deleteline()
        self.insertline(line)
    def deleteline(self):
        self.lines[self.line:self.line+1] = []
    def chmod(self, mode=-1):
	self.mode = mode
    def read(self):
	file_exists = 0
        if os.path.isfile(self.filename):
	    file_exists = 1
	if not self.create_if_missing and not file_exists:
	    raise FileMissing, self.filename + ' does not exist.'
	if file_exists and os.access(self.filename, os.R_OK):
            self.file = open(self.filename, 'r', -1)
            self.lines = self.file.readlines()
            # strip newlines
            for index in range(len(self.lines)):
                self.lines[index] = self.lines[index][:-1]
            self.file.close()
	else:
	    self.lines = []
    def write(self):
	# rcs checkout/checkin errors are thrown away, because they
	# aren't this tool's fault, and there's nothing much it could
	# do about them.  For example, if the file is already locked
	# by someone else, too bad!  This code is for keeping a trail,
	# not for managing contention.  Too many deadlocks that way...
	if self.rcs or os.path.exists(os.path.split(self.filename)[0]+'/RCS'):
	    self.rcs = 1
	    os.system('/usr/bin/co -l '+self.filename+' </dev/null >/dev/null 2>&1')
        self.file = open(self.filename, 'w', -1)
	if self.mode >= 0:
	    os.chmod(self.filename, self.mode)
        # add newlines
        for index in range(len(self.lines)):
            self.file.write(self.lines[index] + '\n')
        self.file.close()
	if self.rcs:
	    mode = os.stat(self.filename)[0]
	    os.system('/usr/bin/ci -u -m"control panel update" ' +
		      self.filename+' </dev/null >/dev/null 2>&1')
	    os.chmod(self.filename, mode)

class ConfShellVar(Conf):
    def __init__(self, filename):
        Conf.__init__(self, filename, commenttype='#',
                      separators='=', separator='=')
    def read(self):
        Conf.read(self)
        self.initvars()
    def initvars(self):
        self.vars = {}
        self.rewind()
        while self.findnextline('^[\t ]*[A-Za-z_][A-Za-z0-9_\[\'\"\]\/]*[\t ]*='):
            self.sedline('[ \t]+=[ \t]*', '=')
            # initialize dictionary of variable/name pairs
            var = self.getfields()
	    # fields 1..n are false separations on "=" character in string,
	    # so we need to join them back together.
	    var[1] = joinfields(var[1:len(var)], '=')
	    if len(var[1]) and var[1][0] in '\'"':
		# found quote; strip from beginning and end
		quote = var[1][0]
		var[1] = var[1][1:]
		p = -1
		try:
		    while cmp(var[1][p], quote):
			# ignore whitespace, etc.
			p = p - 1
		except:
		    raise IndexError, 'end quote not found in '+self.filename+':'+var[0]
		var[1] = var[1][:p]
            self.vars[var[0]] = var[1]
            self.nextline()
        self.rewind()
    def __getitem__(self, varname):
        if self.vars.has_key(varname):
            return self.vars[varname]
        else:
            return ''
    def __setitem__(self, varname, value):
        # set *every* instance of varname to value to avoid surprises
        place=self.tell()
        self.rewind()
        missing=1
        while self.findnextline('[\t ]*' + varname + '[\t ]*=[\t ]*'):
            if re.search('[ \t${}*@!~<>?;%^()#&]', value) > -1:
        	self.sedline('=.*', "='" + value + "'")
	    else:
        	self.sedline('=.*', '=' + value)
            missing=0
            self.nextline()
        if missing:
            self.seek(place)
            if re.search('[ \t${}*@!~<>?;%^()#]', value):
        	self.insertline(varname + "='" + value + "'")
	    else:
        	self.insertline(varname + '=' + value)
        self.vars[varname] = value
    def __delitem__(self, varname):
        # delete *every* instance...
        self.rewind()
        while self.findnextline('[\t ]*' + varname + '='):
            self.deleteline()
	if self.vars.has_key(varname):
            del self.vars[varname]
    def has_key(self, key):
	if self.vars.has_key(key): return 1
	return 0
    def keys(self):
	return self.vars.keys()


import sys, os, string, fnmatch
from socket import gethostname

def set_default(conf, var, value):
    if not conf.has_key(var):
        conf[var] = value

if not os.access("/etc/diskcheck.conf", os.R_OK):
    print "Cannot access configuration file /etc/diskcheck.conf."
    sys.exit(1)
else:
    conf = ConfShellVar("/etc/diskcheck.conf")
    conf.read()
    #print conf.vars

    set_default(conf, 'defaultCutoff', 90)
    #set_default(conf, 'cutoff', {})
    set_default(conf, 'exclude', "/dev/fd*")
    set_default(conf, 'ignore', "")
    set_default(conf, 'mailTo', "root@localhost")
    set_default(conf, 'mailFrom', "Disk Usage Monitor <root>")
    set_default(conf, 'mailProg', "/usr/sbin/sendmail")

    cutoff = {}

    for key in conf.keys():
        if key[:7] == 'cutoff[':
	    seps = '[\'"]+'
            var = regsub.split(key, seps)
            if var and len(var) == 3:
                cutoff[var[1]] = conf[key]
                #print "cutoff[%s] = %s" % (var[1], conf[key])

            
hostname = gethostname()
list = os.popen("df -hP -x none -x tmpfs -x iso9660 %s" % conf['ignore']).readlines()

message = []

message.append("To: %s\n" % conf['mailTo'])
message.append("From: %s\n" % conf['mailFrom'])
message.append("Subject: Low disk space warning\n\n")

message.append("Disk usage for %s:\n\n" % hostname)

high = 0

exlist = regsub.split(conf['exclude'], "[ ]+")

for line in list[1:]:
    (volume, total, used, avail, pct, mountpt) = string.split(line)
    
    nPct = long(pct[:-1])
    mountpt = string.strip(mountpt)


    for rex in exlist:
        if fnmatch.fnmatch(volume, rex):
            do_cont = 1
            break
    else:
        do_cont = 0

    if do_cont == 1:        
        continue

    if cutoff.has_key(volume):
        if (nPct < cutoff[volume]): continue
    elif cutoff.has_key(mountpt):
        if (nPct < cutoff[mountpt]): continue
    elif (nPct < conf['defaultCutoff']): continue

    high = 1
    message.append("%s (%s) is %s full -- %s of %s used, %s remain\n" %
                   (volume, mountpt, pct, used, total, avail))

if (high != 0):
    # mail out the message
    mailer = os.popen("%s -t" % conf['mailProg'], "w")
    for line in message:
        mailer.write(line)

    mailer.close()

sys.exit(0)
