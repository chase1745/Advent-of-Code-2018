import sys
sys.path.append('..')
from adventHelper import FileReader

def formatFreq(freq):
    if freq[0] == '+':
        return int(freq[1:])
    else:
        return -int(freq[1:])

fr = FileReader(1, 2)

freqSet = {0}
frequency = 0
complete = False
while not complete:
    for freq in fr.getlines():
        frequency += formatFreq(freq)
        if frequency in freqSet:
            complete = True
            break
        freqSet.add(frequency)

print("Final frequency: {}".format(frequency))
            