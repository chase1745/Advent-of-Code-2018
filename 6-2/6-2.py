import sys
sys.path.append('..')
from adventHelper import FileReader
from collections import defaultdict
from operator import itemgetter


def format(line):
    line = line.strip().replace(',','').split()
    return (int(line[0]), int(line[1]))

def manhattan(pCoord, qCoord):
    return sum([abs(p - q) for p, q in zip(pCoord, qCoord)])

fr = FileReader(6, 2)

coordinates = list(map(lambda x:format(x), fr.getlines()))
maxX = max(coordinates, key=lambda x:x[0])[0]
maxY = max(coordinates, key=lambda x:x[1])[1]

THRESHOLD = 10000

def getSumDistPoint(i, j):
    return sum([manhattan((i,j),(x,y)) for (y, x) in coordinates])


table = [[0 for _ in range(maxX + 2)] for _ in range(maxY + 2)] # Create table with 0's

# Populate table with coordinates
for i, (y, x) in enumerate(coordinates):
    table[x][y] = i+1 

# Find acceptable region.
safeRegion, area = [], 0
for i in range(len(table)):
    for j in range(len(table[0])):
        sumD = getSumDistPoint(i, j)

        if sumD < THRESHOLD:
            area += 1

print('Area of acceptable range: {}'.format(area))







