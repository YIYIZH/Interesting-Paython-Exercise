#! /usr/bin/python

#print "hello";
import sys
import commands
import fileinput
import re

count = 0
i = 0
s = 0
ll = 0
nn = [0 for x in range(800)]
mm = [[0 for x in range(2)] for x in range(800)]
nn[0] = sys.argv[1]
#mm = [[0]*100,[0]*100,[0]*100]*100
if len(sys.argv) != 2:
        print " "
        print "Usage: python argv[0] argv[1]"
        sys.exit(1)
        print" "
#pattern = r'.*\.(-->).*\+(.*)'
for line in sys.stdin:
    match = line.split("<--")
    mm[i][0] = match[0].strip()
    mm[i][1] = match[1].strip()
    i = i+1

    if not line:
      break

for s in range (0,i):
 for n in range(0,i):
   if mm[n][0] == nn[s]:
     if nn[s] != nn[s-1]:
       nn[s+1] = mm[n][1]
       ll = s

for n in range(ll,-1,-1):
   count = count +1
   print ("%d. %s" % (count,nn[n]))