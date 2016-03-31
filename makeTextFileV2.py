#!/usr/bin/env python

'makeTextFile.py -- create text flie'

import os
ls = os.linesep

# get filename
while True:
    fname = raw_input('please input filename: ')
    if os.path.exists(fname):
        print "ERROR:'%s' already exists" % fname
    else:
        break

# get file content (text) lines
print "\n Enter lines('.' by itself to quit).\n"

fobj = open(fname, 'w')

#loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        fobj.write(entry)
        fobj.write(ls)
        # flush: to prevent data losing
        fobj.flush()

fobj.close()

print 'DONE!'

