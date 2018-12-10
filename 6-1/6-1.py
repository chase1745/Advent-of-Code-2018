import sys
sys.path.append('..')
from adventHelper import FileReader
from collections import defaultdict


def format(line):
    line = line.strip().replace(',','').split()
    return (int(line[0]), int(line[1]))

def manhattan(pCoord, qCoord):
    return sum([abs(p - q) for p, q in zip(pCoord, qCoord)])

fr = FileReader(6, 1)

coordinates = list(map(lambda x:format(x), fr.getlines()))
maxX = max(coordinates, key=lambda x:x[0])[0]
maxY = max(coordinates, key=lambda x:x[1])[1]

def getMinDistPoint(i, j):
    minDist, minDist2, point = None, None, None
    for curr, (y, x) in enumerate(coordinates):
        dist = manhattan((i,j), (x,y))

        try:
            if dist <= minDist:
                point = curr+1
                minDist2 = minDist
                minDist = dist
        except:
            point = curr+1
            minDist = dist
    if minDist == minDist2: # If min point and 2nd min point are tied, return 0
        return 0

    return point


table = [[0 for _ in range(maxX + 2)] for _ in range(maxY + 2)] # Create table with 0's
# print(len(table), len(table[0]))

# Populate table with coordinates
for i, (y, x) in enumerate(coordinates):
    table[x][y] = i+1 

# for i in table:
#     print(i)
# print('\n')

# Find all closest points
for i in range(len(table)):
    for j in range(len(table[0])):
        if table[i][j] > 0: continue

        table[i][j] = getMinDistPoint(i, j)

# for i in table:
#     print(i)

# Get area of points
counts = defaultdict(int)
for i in range(len(table)):
    for j in range(len(table[0])):
        counts[table[i][j]] += 1

# Find finite points
finitePoints = {point:True for point in range(1, len(coordinates)+1)}
i = 0
for j in range(len(table[0])):
    finitePoints[table[i][j]] = False
i = len(table)-1
for j in range(len(table[0])):
    finitePoints[table[i][j]] = False
j = 0
for i in range(len(table)):
    finitePoints[table[i][j]] = False
j = len(table[0])-1
for i in range(len(table)):
    finitePoints[table[i][j]] = False

# Find max area of finite points
maxArea = 0
for point, count in counts.items():
    if point > 0 and finitePoints[point]:
        maxArea = max(maxArea, count)

print('Max area of finite point: {}'.format(maxArea))









