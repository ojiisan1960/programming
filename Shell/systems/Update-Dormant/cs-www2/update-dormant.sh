#!/bin/bash

# Update the other virtual disks

/root/update.www.external.sh
/root/update.graphics.www.sh
/root/update.srv.www.sh

# Shutdown web server and mysql server before copy

/etc/init.d/apache2 stop
/etc/init.d/mysql stop
/root/update.root.sh

# Start web server and mysql server

/etc/init.d/apache2 start

# Start mysql server

/etc/init.d/mysql start
echo Xen machine sync done | mail wogahn@cs.yale.edu -s "$HOSTNAME Xen machine"
