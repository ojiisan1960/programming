"""pathinfo.py:  Object for manipulating information about pathnames
    and their related i-nodes.

    Written by John W. Shipman (john@nmt.edu), New Mexico Tech
    Computer Center, Socorro, NM 87801, in March 1997.

    Freely available under the terms of the GNU General Public
    License.

    This class defines methods for the ten standard components
    of the os.stat() value, giving information about file status.

    Exported methods:
================================================================
    PathInfo(pathName)
        [ if pathname is a valid, existing path name ->
            return a PathInfo representing that path and the
                associated i-node
          else ->
            raise an exception
        ]
    .__str__()
        [ return a string of the form "m  t  p" where:
            m  :=  "drwxrwxrwx" part of `ls -l'
            t  :=  time as "yyyy-mm-dd hh:mm:ss"
            p  :=  pathname used to create self
        ]
    .size()
        [ return self's size as an integer
        ]
    .ownerCanRead()
        [ if owner can read self -> return a nonzero integer
          else -> return 0
        ]
    .ownerCanWrite()
        [ if owner can write self -> return a nonzero integer
          else -> return 0
        ]
    .ownerCanExec()
        [ if owner can execute self -> return a nonzero integer
          else -> return 0
        ]
    .groupCanRead()
        [ if group can read self -> return a nonzero integer
          else -> return 0
        ]
    .groupCanWrite()
        [ if group can write self -> return a nonzero integer
          else -> return 0
        ]
    .groupCanExec()
        [ if group can execute self -> return a nonzero integer
          else -> return 0
        ]
    .worldCanRead()
        [ if world can read self -> return a nonzero integer
          else -> return 0
        ]
    .worldCanWrite()
        [ if world can write self -> return a nonzero integer
          else -> return 0
        ]
    .worldCanExec()
        [ if world can execute self -> return a nonzero integer
          else -> return 0
        ]
    .isDir()
        [ if self is a directory -> return a nonzero integer
          else -> return 0
        ]
    .isLink()
        [ if self is a symbolic link -> return a nonzero integer
          else -> return 0
        ]
    .isFile()
        [ if self is an ordinary disk file -> return a nonzero integer
          else -> return 0
        ]
"""

import os               # Operating system functions
import time             # Functions for handling time
import stat             # Functions for interpreting file status tuples

class PathInfo:
    """Object to represent a pathname and the information from the
        associated inode.
    """

#----------------------------------------------------------------
# State
#----------------------------------------------------------------
# .path == The path passed to __init__
#--
# .stat == The file status tuple
#--
# .mode == The mode bits from the file status tuple
#--

    def __init__ ( self, pathName ):
        self.path  =  pathName
        self.stat  =  os.lstat(pathName)
        self.mode  =  self.stat[stat.ST_MODE]

    def __str__ ( self ):
        baseName = (os.path.split(self.path))[1]
        return ( "%s  %s  %8d %s" %
                 ( self._modeFlags(), self._modTime(), self.size(),
                   baseName ) )

    def _modeFlags ( self ):
        return self._dirFlag() + self._permFlags()

    def _dirFlag ( self ): 
        """ [ if self is a directory -> return "d"
              else if self is a symbolic link -> return "l"
              else if self is a regular file -> return "-"
              else -> return "?"
            ]
        """
        if stat.S_ISLNK(self.mode):
            return "l"
        elif stat.S_ISDIR(self.mode):
            return "d"
        elif stat.S_ISREG(self.mode):
            return "-"
        else:
            return "?"

    def _permFlags ( self ):
        """Return the `rwxrwxrwx' part of ls output
        """
        return ( self._rwx ( self.mode & stat.S_IRUSR,
                             self.mode & stat.S_IWUSR,
                             self.mode & stat.S_IXUSR ) +
                 self._rwx ( self.mode & stat.S_IRGRP,
                             self.mode & stat.S_IWGRP,
                             self.mode & stat.S_IXGRP ) +
                 self._rwx ( self.mode & stat.S_IROTH,
                             self.mode & stat.S_IWOTH,
                             self.mode & stat.S_IXOTH ) )

    def _rwx ( self, r, w, x ):
        """ [ return a string of the form "abc" where:
                a  :=  "r" if r is nonzero, else "-"
                b  :=  "w" if w is nonzero, else "-"
                c  :=  "x" if x is nonzero, else "-"
            ]
        """
        return ( self._dasher ( r, "r" ) +
                 self._dasher ( w, "w" ) +
                 self._dasher ( x, "x" ) )

    def _dasher ( self, b, c ):
        """ [ if b is true -> return c
              else -> return "-"
            ]
        """
        if b:
            return c
        else:
            return "-"

    def _modTime ( self ):
        """ [ return self's modification time as "yyyy-dd-mm hh:mm:ss"
            ]
        """
        return time.strftime ( "%Y-%m-%d %H:%M:%S",
                               time.localtime ( self.stat[stat.ST_MTIME] ) )

    def size ( self ):
        return self.stat[stat.ST_SIZE]

    def ownerCanRead ( self ):
        return self.mode & stat.S_IRUSR

    def ownerCanWrite ( self ):
        return self.mode & stat.S_IWUSR

    def ownerCanExec ( self ):
        return self.mode & stat.S_IXUSR

    def groupCanRead ( self ):
        return self.mode & stat.S_IRGRP

    def groupCanWrite ( self ):
        return self.mode & stat.S_IWGRP

    def groupCanExec ( self ):
        return self.mode & stat.S_IXGRP

    def worldCanRead ( self ):
        return self.mode & stat.S_IROTH

    def worldCanWrite ( self ):
        return self.mode & stat.S_IWOTH

    def worldCanExec ( self ):
        return self.mode & stat.S_IXOTH

    def isDir ( self ):
        return stat.S_ISDIR ( self.mode )

    def isLink ( self ):
        return stat.S_ISLNK ( self.mode )

    def isFile ( self ):
        return stat.S_ISREG ( self.mode )
