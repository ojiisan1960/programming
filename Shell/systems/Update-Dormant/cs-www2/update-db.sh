#!/bin/bash

# Shutdown web server and mysql server before copy
/etc/init.d/mysql stop
/root/update.root.sh
# Start mysql server
/etc/init.d/mysql start
