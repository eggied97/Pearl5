__author__ = 'Egbert'

import time

while 1:
    tStart = time.clock()

    difference = time.clock() - tStart
    if(difference > 0) : print("{} seconden".format(difference))
    #print (difference)
