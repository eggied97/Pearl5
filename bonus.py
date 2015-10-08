__author__ = 'Egbert'

import random
import time

packets = []
queue = []
timeQueue = []
waitTime = []

initArray = 0
maxArrayCount = 100000

chancePcIsSending = 0.2

countPerTimeCycle = 0

while initArray <= maxArrayCount:
    packets.append(initArray)
    initArray += 1

while len(packets) > 0:
    pc1IsSending = random.random() < chancePcIsSending
    pc2IsSending = random.random() < chancePcIsSending
    pc3IsSending = random.random() < chancePcIsSending
    pc4IsSending = random.random() < chancePcIsSending

    if pc1IsSending:
        if len(packets) > 0:
            queue.append("pc1")
            timeQueue.append(time.time())
            countPerTimeCycle += 1
            del packets[-1]

    if pc2IsSending:
        if len(packets) > 0:
            queue.append("pc2")
            timeQueue.append(time.time())
            countPerTimeCycle += 1
            del packets[-1]

    if pc3IsSending:
        if len(packets) > 0:
            queue.append("pc3")
            timeQueue.append(time.time())
            countPerTimeCycle += 1
            del packets[-1]

    if pc4IsSending:
        if len(packets) > 0:
            queue.append("pc4")
            timeQueue.append(time.time())
            countPerTimeCycle += 1
            del packets[-1]

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
        mWaitTime = time.time() - timeQueue[0]
        #print("{} sended, waited {} seconds.".format(queue[0], mWaitTime))
        waitTime.append(mWaitTime)
        del queue[0]
        del timeQueue[0]


    countPerTimeCycle = 0;
    time.sleep(0.0001)

#now print avarege waiting time:
sum = 0;
count = len(waitTime)

while len(waitTime) != 0:
    sum += waitTime[0]
    del waitTime[0]

avarageWaitingTime = sum / count

print("------------------------------------------------")
print("with a total of {} seconds of waitint time".format(sum))
print("this is an avarage of {} seconds per packet".format(avarageWaitingTime))
print("------------------------------------------------")





