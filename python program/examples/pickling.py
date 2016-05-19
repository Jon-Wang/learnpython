#!/usr/bin/python
# Filename: pickling.py

import cPickle as P
#import Pickle as P

shoplistfile = 'shoplist.data'
# the name of file where we will store the object

shoplist = ['apple','mango','carrot']

# Writeto the file
f =file(shoplistfile,'w')
P.dump(shoplist,f) # dump the obeject to a file

del shoplist #remove the shoplist

#Readback from the storage
f = file(shoplistfile)
storedlist = P.load(f)
print storedlist
