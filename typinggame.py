import random
import time

def toRun(toType):
    while True:
        var = input(toType.__str__() + n)
        if var != toType:
            return 0
        else:
            return 1

def timeForThing():
    numCorrect = 0
    start = time.time()
    while toRun(list[random.randint(0, list.__len__()-1)]) != 0:
        numCorrect += 1
    end = time.time()
    return end-start, numCorrect

list = []
for i in range(ord('a'), ord('z')+1):
    list.append(chr(i))

timeTaken, numCompleted = timeForThing()

print(You type at {} words per minute!.format(numCompleted/(timeTaken/60)))
