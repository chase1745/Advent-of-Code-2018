import sys
sys.path.append('..')
from adventHelper import FileReader
import pandas as pd
from collections import defaultdict

def getWidth(lineSplit):
    return int(lineSplit[3].split('x')[0])

def getHeight(lineSplit):
    return int(lineSplit[3].split('x')[1])

def getLeftInches(lineSplit):
    return int(lineSplit[2].split(',')[0])

def getTopInches(lineSplit):
    return int(lineSplit[2].split(',')[1].strip(':'))

def getId(lineSplit):
    return lineSplit[0][1:]

def dfs(fabric, x, y):
    h, w = idToHW[squareToId[(x,y)][0]]
    for i in range(x,x+h):
        for j in range(y,y+w):
            if fabric[i][j] != 1:
                return False
    return True

fr = FileReader(3, 2)
fabric = [[0 for i in range(1001)] for i in range(1001)]
squareToId = defaultdict(list)
idToHW = {}

for lineSplit in map(lambda x : x.split(), fr.getlines()):
    widthInterval = (getLeftInches(lineSplit), getLeftInches(lineSplit) + getWidth(lineSplit))
    heightInterval = (getTopInches(lineSplit), getTopInches(lineSplit) + getHeight(lineSplit))
    idToHW[getId(lineSplit)] = (getHeight(lineSplit), getWidth(lineSplit))

    for i in range(heightInterval[0], heightInterval[1]):
        for j in range(widthInterval[0], widthInterval[1]):
            squareToId[(i,j)].append(getId(lineSplit))
            fabric[i][j] += 1

claim = None
for i in range(len(fabric)):
    for j in range(len(fabric)):
        if fabric[i][j] == 1:
            if dfs(fabric, i, j):
                if claim is not None:
                    print(claim)
                    claim = squareToId[(i,j)][0]
                claim = squareToId[(i,j)][0]
                # break
    # if claim is not None: break


print("Claim with no overlaps: " + claim)        