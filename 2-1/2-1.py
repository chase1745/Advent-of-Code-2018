import sys
sys.path.append('..')
from adventHelper import FileReader

fr = FileReader(2, 1)

doubleCount, tripleCount = 0, 0
for line in fr.getlines():
    doubleFound, tripleFound = False, False
    for char in set(line):
        if doubleFound and tripleFound: break
        if not doubleFound and line.count(char) == 2:
            doubleCount += 1
            doubleFound = True
        elif not tripleFound and line.count(char) == 3:
            tripleCount += 1
            tripleFound = True

print("Checksum: {}".format(doubleCount * tripleCount))