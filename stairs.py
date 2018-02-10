"""
Usage:
$ python3 stairs.py 10
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########
 #########
##########
"""

import sys

def errorHandler():
    print("Ожидается число")
    exit(1)


if sys.argv.__len__() < 2:
    errorHandler()


nsteps = int(sys.argv[1])

step = 1
for i in range(nsteps):
    s = (" " * (nsteps -step)) + ("#" * step)
    step += 1
    print(s)


