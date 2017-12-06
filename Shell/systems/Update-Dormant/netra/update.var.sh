#!/bin/bash
# hacked to use rsyncd

#echo "
# Default definitions
HOSTNAME=`hostname -s`
XENHOSTS="mother supermax"
IMAGE_DIR="/var/lib/xen/images"
# 
MNT_DIR_ROOT="/mnt/$HOSTNAME/var"
#
RSYNC="rsync --delete -avx"

# system image definitions
ROOT_DISK_IMAGE="$HOSTNAME.var.img"
MOUNT_ROOT_IMAGE="lomount -diskimage $IMAGE_DIR/$ROOT_DISK_IMAGE -partition 1 $MNT_DIR_ROOT"
ROOT_DIRS="/var/"


# Find out which server is hosting this system and sync to the other
#for i in mother supermax
for i in $XENHOSTS
do
	ssh $i xm list $HOSTNAME > /dev/null 2>&1
	if [ $? -eq 1 ];then
		if [ $i = 'mother' ];then
		SYNC_HOST='mother'
		CUR_HOST='supermax'
		elif [ $i = 'supermax' ];then
		SYNC_HOST='supermax'
		CUR_HOST='mother'
		fi
	fi
done

echo ""
echo $HOSTNAME is running on $CUR_HOST will sync with $SYNC_HOST

# Test for disk image
echo ""
echo "Test for disk image..."
echo ""
ssh $SYNC_HOST [ -w $IMAGE_DIR/$ROOT_DISK_IMAGE ]
	if [ $? -eq 1 ];then
	echo "Disk image $ROOT_DISK_IMAGE does not exist!"
	exit 1
	else
	echo "Disk image $ROOT_DISK_IMAGE exists and is writable"
	fi

# Test for mount point
echo ""
echo "Test for mount point..."
echo ""
ssh $SYNC_HOST [ -d $MNT_DIR_ROOT ]
	if [ $? -eq 1 ];then
	echo "Mount dir $MNT_DIR_ROOT does not exist"
	exit 1
	else
	echo "Mount point exists"
	echo "Testing to see if the disk image is already mounted..."
	fi

# See if the disk image is mounted
echo ""
ssh $SYNC_HOST [ -d $MNT_DIR_ROOT/lost+found ]
    if [ $? -eq 0 ];then
        echo "$ROOT_DISK_IMAGE seems to be mounted"
        echo ""
    else
        echo "Disk image not mounted proceeding with mount..."
	echo ""
	echo ssh $SYNC_HOST $MOUNT_ROOT_IMAGE
	ssh $SYNC_HOST $MOUNT_ROOT_IMAGE
    	if [ $? -gt 0 ];then
        	echo "Disk image mount failed!"
        	exit 1
    	else
        	echo "Disk image mount sucess"
    	fi
    fi

# Sync with host
echo "Sync with $SYNC_HOST..."
echo $RSYNC $ROOT_DIRS $SYNC_HOST::images/$HOSTNAME/
$RSYNC $ROOT_DIRS $SYNC_HOST::images/$HOSTNAME/
    if [ $? -gt 0 ];then
        echo "Sync failed with error: $? !"
    else
        echo "Sync finished"
    fi

echo ""

# Unmount disk image
echo ssh $SYNC_HOST umount $MNT_DIR_ROOT
ssh $SYNC_HOST umount $MNT_DIR_ROOT

# Update Xen conf from running system
echo "Copying Xen conf..."
scp $CUR_HOST:/etc/xen/$HOSTNAME $SYNC_HOST:/etc/xen/ 
echo ""
echo $HOSTNAME is synchronized on $SYNC_HOST
echo ""
exit 0
#"
