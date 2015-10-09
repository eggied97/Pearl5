__author__ = 'Egbert'

import random
import time

queue = []
timeQueue = []
waitTime = []

packetCount = 100000

chancePcIsSending = 0.25

countPerTimeCycle = 0

timePerTick = 0.0001

numberOfComputers = 4;


while packetCount > 0:

    i = numberOfComputers

    while i > 0:
        if random.random() < chancePcIsSending:
            if packetCount > 0:
                queue.append("pc{}".format(i))
                timeQueue.append(time.clock())
                countPerTimeCycle += 1
                packetCount -= 1

        i -= 1


    if (countPerTimeCycle == 1) & (len(queue) == 1):
        #print("{} sended, no waiting time because he was the only one.".format(queue[0]))
        del queue[0]
        del timeQueue[0]
        waitTime.append(0)
    elif len(queue) == 0:
        #print("queue is empty")
        1 == 1

    else:
        #grab from the queue
        mWaitTime = time.clock() - timeQueue[0]
        #print("{} sended, waited {} seconds.".format(queue[0], mWaitTime))
        waitTime.append(mWaitTime)
        del queue[0]
        del timeQueue[0]


    countPerTimeCycle = 0;
    time.sleep(timePerTick)

#empty the queue, if we have any
while len(queue) > 0:

    mWaitTime = time.clock() - timeQueue[0]
    waitTime.append(mWaitTime)
    del queue[0]
    del timeQueue[0]
    time.sleep(timePerTick)


#now print avarege waiting time:
sum = 0;
count = len(waitTime)

while len(waitTime) > 0:
    sum += waitTime[0]
    del waitTime[0]



avarageWaitingTime = sum / count

print("------------------------------------------------")
print("with a total of {} seconds of waitint time".format(sum))
print("this is an avarage of {} seconds per packet".format(avarageWaitingTime))
print("------------------------------------------------")





