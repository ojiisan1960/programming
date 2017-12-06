#!/bin/sh

# Long list of all packages, should be taken from the manifest
package_list="
RedHat Linux 6.1 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh61up.i386.rpm MD5SUM: 83aeddef6569efc8d623cfb81e06e97d

RedHat Linux 6.2 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh62up.i386.rpm MD5SUM: b055e70b286e19826509ec7b447d2c1e

SuSE Linux 6.4 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.suse64up.i386.rpm MD5SUM: e336de17488a0146e4463936215518e9

SuSE Linux 6.4 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.suse70up.i386.rpm MD5SUM: 0fad9b6a2bf14ba4285a81fc8a72e9d7

Mandrake Linux 7.1 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk71up.i386.rpm MD5SUM: 91de543d9a1ab09416a9575e22363959

Mandrake Linux 7.2 UP Single Processor System i386 Architecture
NVIDIA_kernel-1.0-2960.mdk72up.i386.rpm MD5SUM: 442ffce96ee26b952d7d36ef33ce8fab

RedHat Linux 6.1 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.rh61smp.i386.rpm MD5SUM: 2b5dbf1804573bdccb93de1bfd032a0a

RedHat Linux 6.2 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.rh62smp.i386.rpm MD5SUM: 98993177038d4597eb9ce45d7271356f

SuSE Linux 6.4 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.suse64smp.i386.rpm MD5SUM: b382d49cc675849db95e72b3e7a710fb

SuSE Linux 7.0 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.suse70smp.i386.rpm MD5SUM: c8896d49b65e65f9a664153cbc87d0d6

Mandrake Linux 7.1 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk71smp.i386.rpm MD5SUM: 0f41a4b859b4fafc8b883063828fcacc

Mandrake Linux 7.2 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk72smp.i386.rpm MD5SUM: 443855611aaa402881391bc11f99258e

RedHat Linux 7.0 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh70up.i386.rpm MD5SUM: 92d280b2b15ee51a789b5887f45ca0bf

RedHat Linux 7.0 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.rh70smp.i386.rpm MD5SUM: c54e04dd67d3d60b31e2faa9dddbf39c

RedHat Linux 7.1 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh71up.i386.rpm MD5SUM: 40bea307896718ae36d34415ce5abf31

RedHat Linux 7.1 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.rh71smp.i386.rpm MD5SUM: 0749f9b66ee45efa12e9664b3666b5d0

RedHat Linux 7.2 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh72up.i386.rpm MD5SUM: 6b5f682b4e2421191c552408c25532f6

RedHat Linux 7.2 updated to 2.4.9-31 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh72up_2.4.9_31.i386.rpm MD5SUM: 24fb54d4b9541ca3b82025b099787f21

RedHat Linux 7.3 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.rh73up.i386.rpm MD5SUM: 7d1d768bb836dcd55b48cc814ab1b8ce

Mandrake Linux 8.0 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk80up.i386.rpm MD5SUM: d6ea356488b781b171629f98c6d7670b

Mandrake Linux 8.0 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk80smp.i386.rpm MD5SUM: f4b71577378a190658d595246d9837d9

Mandrake Linux 8.1 UP Single Processor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk81up.i386.rpm MD5SUM: 94811f6cffc9e566b879a2610e996152

Mandrake Linux 8.1 SMP Multiprocessor i386 Architecture
NVIDIA_kernel-1.0-2960.mdk81smp.i386.rpm MD5SUM: db1a43cafecfc589dc4723fb11da7ccd

RedHat Linux 7.0 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.rh70up.i686.rpm MD5SUM: e61aca91f7c034af24f499fdd01b8b35

RedHat Linux 7.0 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.rh70smp.i686.rpm MD5SUM: ed94ab1b0c8b5c72969c22592791fcad

RedHat Linux 7.0 Enterprise on i686 Architecture
NVIDIA_kernel-1.0-2960.rh70enterprise.i686.rpm MD5SUM: b3c8082f45c96a349c92f92689034546

RedHat Linux 7.1 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.rh71up.i686.rpm MD5SUM: c8c53f93572cd3003e9e5487b504e370

RedHat Linux 7.1 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.rh71smp.i686.rpm MD5SUM: 4c8c2e453f5416422a612ec2f46154d4

RedHat Linux 7.1 Enterprise i686 Architecture
NVIDIA_kernel-1.0-2960.rh71enterprise.i686.rpm MD5SUM: 20b77548be7f70089c3f6e6dd0ca7261

RedHat Linux 7.2 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.rh72up.i686.rpm MD5SUM: 00d6e7d76f62f82c4a43486519399274

RedHat Linux 7.2 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.rh72smp.i686.rpm MD5SUM: 3f157e0dc3151d4d4536c97cc45745b1

RedHat Linux 7.2 Enterprise i686 Architecture
NVIDIA_kernel-1.0-2960.rh72enterprise.i686.rpm MD5SUM: f50055f00cc7871e29e9b30450d9c132

RedHat Linux 7.2 updated to 2.4.9-31 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.rh72up_2.4.9_31.i686.rpm MD5SUM: 7e4add8e5d9ff905d9b8e07e00b2b5e2

RedHat Linux 7.2 updated to 2.4.9-31 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.rh72smp_2.4.9_31.i686.rpm MD5SUM: 49717b27d9766747c1e7710eac3874b1

RedHat Linux 7.2 updated to 2.4.9-31 Enterprise i686 Architecture
NVIDIA_kernel-1.0-2960.rh72enterprise_2.4.9_31.i686.rpm MD5SUM: 3ce69d881852564384563e6a368acbbf

RedHat Linux 7.3 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.rh73up.i686.rpm MD5SUM: b89d4b88d80d79658c55026911c5dc3b

RedHat Linux 7.3 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.rh73smp.i686.rpm MD5SUM: b6b623be8ffadf061852bdc68eacb572

RedHat Linux 7.3 Bigmem i686 Architecture
NVIDIA_kernel-1.0-2960.rh73bigmem.i686.rpm MD5SUM: f0e7cd7b53c97959b2051d1176d7c4ac

Mandrake Linux 8.0 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.mdk80up.i686.rpm MD5SUM: 68daa589e541a374d86f9ede3716aa2f

Mandrake Linux 8.0 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.mdk80smp.i686.rpm MD5SUM: b3a5979789f0b2e17d9c678372395d4f

Mandrake Linux 8.0 Enterprise i686 Architecture
NVIDIA_kernel-1.0-2960.mdk80enterprise.i686.rpm MD5SUM: 523cf25e5afcbee3d374d12775633a90

Mandrake Linux 8.1 UP Single Processor i686 Architecture
NVIDIA_kernel-1.0-2960.mdk81up.i686.rpm MD5SUM: 6f34f405a357f004310fd3761a970538

Mandrake Linux 8.1 SMP Multiprocessor i686 Architecture
NVIDIA_kernel-1.0-2960.mdk81smp.i686.rpm MD5SUM: dd1c29aabbcc248f3987f4addec2e693

Mandrake Linux 8.1 Enterprise i686 Architecture
NVIDIA_kernel-1.0-2960.mdk81enterprise.i686.rpm MD5SUM: 5c8a76aec96d402188c7c7c9bc302b92

RedHat Linux 7.2 UP Single Processor Athlon Architecture
NVIDIA_kernel-1.0-2960.rh72up.athlon.rpm MD5SUM: 38fe272a03127cbe8740a44fa4e41008

RedHat Linux 7.2 SMP Multiprocessor Athlon Architecture
NVIDIA_kernel-1.0-2960.rh72smp.athlon.rpm MD5SUM: 452b809146d9a2d5b5905cdadb233289

RedHat Linux 7.2 updated to 2.4.9-31 UP Single Processor Athlon Architecture
NVIDIA_kernel-1.0-2960.rh72up_2.4.9_31.athlon.rpm MD5SUM: 530a3ea46a7b4d59283e4b25d82c081f

RedHat Linux 7.2 updated to 2.4.9-31 SMP Multiprocessor Athlon Architecture
NVIDIA_kernel-1.0-2960.rh72smp_2.4.9_31.athlon.rpm MD5SUM: 3717b335f13ca743eb1439fbe6961634

RedHat Linux 7.3 UP Single Processor Athlon Architecture
NVIDIA_kernel-1.0-2960.rh73up.athlon.rpm MD5SUM: 942875b5aef33c374a32d91a994cf01e

RedHat Linux 7.3 SMP Multiprocessor Athlon Architecture
NVIDIA_kernel-1.0-2960.rh73smp.athlon.rpm MD5SUM: eece9e100df2a529067bb29295a09694

RedHat Linux 7.3 SMP Multiprocessor i586 Architecture
NVIDIA_kernel-1.0-2960.rh73smp.i586.rpm MD5SUM: 96fce4b343323f2048562dc6989029b3

Mandrake Linux 8.2 UP Single Processor i586 Architecture
NVIDIA_kernel-1.0-2960.mdk82up.i586.rpm MD5SUM: 9a59b961a979b7315ae1599ed0c721f3

Mandrake Linux 8.2 SMP Multiprocessor i586 Architecture
NVIDIA_kernel-1.0-2960.mdk82smp.i586.rpm MD5SUM: 6ca220b56acee7e4326e18c679ab1991

Mandrake Linux 8.1 Enterprise i586 Architecture
NVIDIA_kernel-1.0-2960.mdk82enterprise.i586.rpm MD5SUM: 66c9c07adfb832a38c474e5ea4453a04

Mandrake Linux 8.2 Secure i586 Architecture
NVIDIA_kernel-1.0-2960.mdk82secure.i586.rpm MD5SUM: 55f0990a3e55ef6b9b068fc0883b1e71

Common X and OpenGL for all Linux systems.
NVIDIA_GLX-1.0-2960.i386.rpm MD5SUM: 41f1be196298c78a1ecb771517b81f1b

For systems not listed above
NVIDIA_kernel-1.0-2960.src.rpm MD5SUM: 507ef3016b0ee6a05425cf7845604e39
NVIDIA_GLX-1.0-2960.src.rpm MD5SUM: dfa37312eae92bd993ff88fa82dde6ea

For systems that don't use RPM
NVIDIA_kernel-1.0-2960.tar.gz MD5SUM: 372a72010e8a1659454330cc7f5a490f
NVIDIA_GLX-1.0-2960.tar.gz MD5SUM: 38947e44a19a576c2ab8e648e1f3cf18
"

# Driver Version
NVVERSION=1.0-2960

# Determine which distribution and version is running

# Is it Red Hat? 
# Red Hat's issue looks like "Red Hat Linux release X.Y (codename)
if ( grep "Red Hat" /etc/issue > /dev/null ); then
    distro="rh"
    version=`grep "Red Hat" /etc/issue  | tr -d "a-zA-Z(). "`
fi

# Is it Mandrake?
# Mandrake's issue has a big logo in it and then
# "Mandrake Linux release X.Y (codename) for some_arch
if ( grep "Mandrake" /etc/issue > /dev/null ); then
    distro="mdk"
    version=`grep "Mandrake" /etc/issue | sed -e "s/.*release \([0-9]\+\)\.\([0-9]\+\).*/\1\2/"`
fi

# Is it SuSE?
# 
if [ -f /etc/SuSE-release ]; then
  version=`grep VERSION /etc/SuSE-release|tr -d "a-zA-Z =."`
  [ "$version" = "70" ] && version="70+xfree86-4.0.2"
  KERNEL_PACKAGE=NVIDIA_kernel-${NVVERSION}.suse${version}.i386.rpm
  GLX_PACKAGE=NVIDIA_GLX-${NVVERSION}.suse${version}.i386.rpm
  echo "Please download and install the following files:"
  echo $GLX_PACKAGE
  echo $KERNEL_PACKAGE
  exit 0
fi

# XXX Detect Debian and recommend either the tarball or link to the
# Debian contrib package.

# XXX Other distros, recommend the tar ball
if [ -z "$distro" ]; then
    echo "NVIDIA does not provide a prebuilt binary driver for your"
    echo "distribution at this time.  Please download:"
    echo $package_list | tr " " "\n" | grep "tar.gz" | cut -f 1 -d " "
    exit
fi

# XXX Make this support command line options to specify a kernel that isn't
# the running kernel.

# Determine architecture (strip mdk out if its present)
KERNEL_TYPE=`uname -r | tr -d "0-9.-" | sed -e "s/mdk//"`
KERNEL_VERSION=`uname -r | tr -d "a-zA-Z"`
KERNEL_PACKAGE=kernel
if [ -n "$KERNEL_TYPE" ]; then
    KERNEL_PACKAGE=$KERNEL_PACKAGE-$KERNEL_TYPE
fi
if [ -n "$KERNEL_VERSION" ]; then
    KERNEL_PACKAGE=$KERNEL_PACKAGE-$KERNEL_VERSION
    # On mandrake we have to add mdk to the version (it was in the uname but 
    # we stripped it out with  tr above, we want to strip it out because
    # it has other stuff as well)
    if [ "$distro" = "mdk" ]; then 
        KERNEL_PACKAGE=${KERNEL_PACKAGE}mdk
    fi
fi

# Which kernel, matching the above, is actually installed?  Get the arch
# from it.  Default to something that can't match
KERNEL_ARCH="unknown"
# rpm will emit error text to stdout if it doesn't find what I asked for, 
# so  we have to check the return value.
rpm -q --qf '%{ARCH}' $KERNEL_PACKAGE > /dev/null && KERNEL_ARCH=`rpm -q --qf '%{ARCH}' $KERNEL_PACKAGE`
if [ "$KERNEL_ARCH" = "unknown" ]; then
    # Try some other variations, since some distro's name their
    # packages in different way's
    TMP_KERNEL_VERSION=`echo $KERNEL_VERSION | tr "-" "."`
    KERNEL_PACKAGE="kernel-$TMP_KERNEL_VERSION"
    if [ "$distro" = "mdk" ]; then
	KERNEL_PACKAGE=${KERNEL_PACKAGE}mdk
    fi
    rpm -q --qf '%{ARCH}' $KERNEL_PACKAGE > /dev/null && KERNEL_ARCH=`rpm -q --qf '%{ARCH}' $KERNEL_PACKAGE`
fi

# Fixup KERNEL_VERSION change '-' to '_' since that's the way the RPM is 
# named. (For whatever reason RPM didn't allow a - in that field in the name.)
KERNEL_VERSION=`echo $KERNEL_VERSION | tr "-" "_"`

# Ok, lots of rules for patching up the ARCH
# 1) We only have i386 builds for things that aren't one of
#    - RedHat 7.2 or later
#    - Mandrake 8.1 or later
#    - enterprise kernels
# 2) We don't do i586 builds, except on Mandrake 8.2, they get promoted to i686
if [ \( "$distro" = "rh"  -a "$version" -ge 72 \) -o \
     \( "$distro" = "mdk" -a "$version" -eq 81 \) -o \
     \( "$KERNEL_TYPE" = "enterprise" \) ]; then
    # We have i686/athlon builds, promote i586 builds to i686
    KERNEL_ARCH=`echo $KERNEL_ARCH | sed -e "s/i586/i686/"`
elif [ \( "$distro" = "mdk" -a "$version" -ge 82 \) ]; then
    # Do nothing, just stay our of the default case
    echo -n
elif [ "$KERNEL_ARCH" != "unknown" ]; then
    # We just have i386 builds
    KERNEL_ARCH="i386"
fi


# Two different naming styles, one for update kernels, one for standard 
# kernels.  We append "up" if there is no type
if [ -z "$KERNEL_TYPE" ]; then
    KERNEL_TYPE=up
fi
UPDATE_PACKAGE=NVIDIA_kernel-${NVVERSION}.${distro}${version}${KERNEL_TYPE}_${KERNEL_VERSION}.${KERNEL_ARCH}.rpm
STANDARD_PACKAGE=NVIDIA_kernel-${NVVERSION}.${distro}${version}${KERNEL_TYPE}.${KERNEL_ARCH}.rpm
GLX_PACKAGE=NVIDIA_GLX-${NVVERSION}.i386.rpm

echo "Please download and install the following files:"
# First assume we have an update kernel and see if its in the list
if echo -e $package_list | tr " " "\n" | grep "$UPDATE_PACKAGE" > /dev/null ; then
    echo $UPDATE_PACKAGE
# If its not an update kernel then try it as a standard kernel
elif echo -e $package_list | tr " " "\n" | grep "$STANDARD_PACKAGE" > /dev/null ; then
    echo $STANDARD_PACKAGE
else
    # if its not a standard kernel or an update kernel then recommend the
    # src rpm
    echo $package_list | tr " " "\n" | grep "NVIDIA_kernel.*src\.rpm" | \
            cut -f 1 -d " "
fi
echo $GLX_PACKAGE
