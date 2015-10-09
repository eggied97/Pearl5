__author__ = 'Egbert'

import random

#-----------------------------------------------
#   Initializing the variables
#-----------------------------------------------

queue = []
timeQueue = []
waitTime = []

packetCount = 100000        #Number of packets that we have
chancePcIsSending = 0.25    #Chance that a computer is sending a packet
countPerTimeCycle = 0       #counter to keep track of the computers have send in that tick
ticks = 0                   #Number of total ticks
numberOfComputers = 4       #Number of computers


while packetCount > 0:      #Loop till all the packets are gone

    i = numberOfComputers   #For the initializing of the pc's

    while i > 0:
        if random.random() < chancePcIsSending:
            if packetCount > 0:                     #In the case we have 2 packets in the beginning, but >2 computers want to send a packet.
                queue.append("pc{}".format(i))      #Add which computer is sending to the array
                timeQueue.append(ticks)             #And on which tick he has send the packet
                countPerTimeCycle += 1
                packetCount -= 1

        i -= 1


    if (countPerTimeCycle == 1) & (len(queue) == 1): #If there is only 1 packet send this tick, and the queue only contains this packet
        del queue[0]        #delete the packet
        del timeQueue[0]    #delete from the ticksArray
        waitTime.append(0)  #add 0 to the totalTimeArray, because he had no waiting time
    elif len(queue) == 0:
        1 == 1 #if the queue is empty, couldnt leave this blank

    else:
        #Now we grab the first item from the timeArray, and decide how long it needed to wait.
        mWaitTime = ticks - timeQueue[0]
        waitTime.append(mWaitTime)  #then we apped this to our totalTimeArray
        del queue[0]                #And delete the computer and tickCount from our array
        del timeQueue[0]


    countPerTimeCycle = 0   #reset this variable, because the tick is over
    ticks += 1              #Tick = tick + 1


#-----------------------------------------------
#All Our packets are used, but we might still have a queue, so we check this and empty it if needed.
#-----------------------------------------------
while len(queue) > 0:
    mWaitTime = ticks - timeQueue[0]
    waitTime.append(mWaitTime)
    del queue[0]
    del timeQueue[0]
    ticks +=1

#-----------------------------------------------
#Now we need to make the sum of the total waiting time.
#-----------------------------------------------

sum = 0
while len(waitTime) > 0:
    sum += waitTime[0]
    del waitTime[0]



avarageWaitingTime = sum / ticks #And the avarage waiting time

print("------------------------------------------------")
print("with a total of {} ticks of waitint time".format(sum))
print("with {} ticks".format(ticks))
print("this is an avarage of {} ticks per packet".format(avarageWaitingTime))
print("------------------------------------------------")





