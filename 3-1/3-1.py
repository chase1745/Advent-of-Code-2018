import sys
sys.path.append('..')
from adventHelper import FileReader
import pandas as pd

def getWidth(lineSplit):
    return int(lineSplit[3].split('x')[0])

def getHeight(lineSplit):
    return int(lineSplit[3].split('x')[1])

def getLeftInches(lineSplit):
    return int(lineSplit[2].split(',')[0])

def getTopInches(lineSplit):
    return int(lineSplit[2].split(',')[1].strip(':'))

fr = FileReader(3, 1)
fabric = [[0 for i in range(1001)] for i in range(1001)]
print(len(fabric), len(fabric[0]))

for lineSplit in map(lambda x : x.split(), fr.getlines()):
    widthInterval = (getLeftInches(lineSplit), getLeftInches(lineSplit) + getWidth(lineSplit))
    heightInterval = (getTopInches(lineSplit), getTopInches(lineSplit) + getHeight(lineSplit))
    print(heightInterval, widthInterval)

    for i in range(heightInterval[0], heightInterval[1]):
        for j in range(widthInterval[0], widthInterval[1]):
            fabric[i][j] += 1

count = 0
for i in range(len(fabric)):
    for j in range(len(fabric)):
        if fabric[i][j] > 1:
            count += 1


print("Total square inches overlapping: {}".format(count))

