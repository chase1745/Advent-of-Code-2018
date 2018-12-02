import sys
sys.path.append('..')
from adventHelper import FileReader

def formatFreq(freq):
    if freq[0] == '+':
        return int(freq[1:])
    else:
        return -int(freq[1:])

fr = FileReader(1, 1)

frequencies = 0
for freq in fr.getlines():
    frequencies += formatFreq(freq)

print("Final frequency: {}".format(frequencies))