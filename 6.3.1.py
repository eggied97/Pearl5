__author__ = 'Egbert'

import time

i = 1000000
j = 0

while 1:
    start = time.clock()

    while j <= i:
        j += 1

    duration = time.clock() - start

    j = 0;

    print("{} seconden".format(duration))