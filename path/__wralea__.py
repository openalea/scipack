from openalea.core import Factory as Fa
from openalea.core import IDirStr, IFileStr, IInt, IStr

__name__ = 'openalea.path'

__editable__ = True
__description__ = 'File manipulation library.'
__license__ = 'CECILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__version__ = '0.0.1'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__icon__ = ''

__all__ = []

abspath = Fa(uid="bdce27864e7611e6bff6d4bed973e64a",
             name='abspath',
             category='File,IO',
             nodemodule='openalea.path.paths',
             nodeclass='py_abspath',
             inputs=({'interface': IFileStr, 'name': 'path', 'value': '.'},),
             outputs=({'interface': IFileStr, 'name': 'path'},),
             )
__all__.append('abspath')

basename = Fa(uid="bdce27874e7611e6bff6d4bed973e64a",
              name='basename',
              category='File,IO',
              nodemodule='openalea.path.paths',
              nodeclass='py_basename',
              inputs=({'interface': IFileStr, 'name': 'path', 'value': '.'},),
              outputs=({'interface': IFileStr, 'name': 'path'},),
              )
__all__.append('basename')

bytes_ = Fa(uid="bdce27884e7611e6bff6d4bed973e64a",
            name='bytes',
            category='File,IO',
            nodemodule='openalea.path.paths',
            nodeclass='py_bytes',
            inputs=({'interface': IFileStr, 'name': 'path', 'value': '.'},),
            outputs=({'interface': IStr, 'name': 'content'},),
            )
__all__.append('bytes_')

chmod = Fa(uid="bdce27894e7611e6bff6d4bed973e64a",
           name='chmod',
           category='File,IO',
           nodemodule='openalea.path.paths',
           nodeclass='py_chmod',
           inputs=({'interface': IFileStr, 'name': 'path', 'value': '.'},
                   dict(name='mode', interface=IInt, value=755)),
           outputs=({'interface': IFileStr, 'name': 'path'},),
           )
__all__.append('chmod')

chown = Fa(uid="bdce278a4e7611e6bff6d4bed973e64a",
           name='chown',
           category='File,IO',
           nodemodule='openalea.path.paths',
           nodeclass='py_chown',
           inputs=({'interface': IFileStr, 'name': 'path', 'value': '.'},
                   dict(name='uid', interface=IInt),
                   dict(name='gid', interface=IInt)),
           outputs=({'interface': IFileStr, 'name': 'path'},),
           )
__all__.append('chown')

copy = Fa(uid="bdce278b4e7611e6bff6d4bed973e64a",
          name='copy',
          category='File,IO',
          nodemodule='openalea.path.paths',
          nodeclass='py_copy',
          inputs=({'interface': IFileStr, 'name': 'src', 'value': '.'},
                  {'interface': IFileStr, 'name': 'dest', 'value': '.'},),
          outputs=({'interface': IFileStr, 'name': 'path'},),
          )
__all__.append('copy')

copy_dir = Fa(uid="bdce278c4e7611e6bff6d4bed973e64a",
              name='copy (dir)',
              category='File,IO',
              nodemodule='openalea.path.paths',
              nodeclass='py_copy',
              inputs=({'interface': IFileStr, 'name': 'src', 'value': '.'},
                      {'interface': IDirStr, 'name': 'dest', 'value': '.'},),
              outputs=({'interface': IFileStr, 'name': 'path'},),
              )
__all__.append('copy_dir')

"""
copy
copy2
copyfile
copymode
copystat
copytree
count
ctime
decode
dirname
dirs
drive
encode
endswith
exists
expand
expandtabs
expanduser
expandvars
ext
files
find
fnmatch
format
get_owner
getatime
getctime
getcwd
getmtime
getsize
glob
index
isabs
isalnum
isalpha
isdigit
isdir
isfile
islink
islower
ismount
isspace
istitle
isupper
join
joinpath
lines
link
listdir
ljust
lower
lstat
lstrip
makedirs
mkdir
move
mtime
name
namebase
normcase
normpath
open
owner
parent
partition
pathconf
read_md5
readlink
readlinkabs
realpath
relpath
relpathto
remove
removedirs
rename
renames
replace
rfind
rindex
rjust
rmdir
rmtree
rpartition
rsplit
rstrip
samefile
size
split
splitall
splitdrive
splitext
splitlines
splitpath
startswith
stat
statvfs
strip
stripext
swapcase
symlink
text
title
touch
translate
unlink
upper
utime
walk
walkdirs
walkfiles
write_bytes
write_lines
write_text
zfill
"""
