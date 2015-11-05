#read files

from __future__ import with_statement #for python 2.5
with open('C:/path/numbers.txt', 'r') as f:
    lines = f.readlines()