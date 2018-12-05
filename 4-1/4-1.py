import sys
sys.path.append('..')
from adventHelper import FileReader
from collections import defaultdict
import re


def format(line):
    date = re.compile('\d{4}-\d{2}-\d{2}').search(line).group(0)
    hour = int(re.compile('\d{2}(?=:\d{2})').search(line).group(0))
    minute = int(re.compile('(?<=\d{2}:)\d{2}').search(line).group(0))
    typeEntry = ''
    if 'wakes' in line:
        typeEntry = 'awake'
    elif 'falls' in line:
        typeEntry = 'asleep'
    else:
        typeEntry = int(re.compile('(?<=#)\d*').search(line).group(0))

    return date, hour, minute, typeEntry

fr = FileReader(4, 1)
lines = sorted([l for l in fr.getlines()])

guardAsleepMin = defaultdict(lambda: defaultdict(int))
guardAsleepCount = defaultdict(int)
for (date, hour, minute, typeEntry) in map(lambda x:format(x), lines):
    if type(typeEntry) == int:
        guard = typeEntry
    elif typeEntry == 'asleep':
        guardAsleepMin[guard][minute] += 1
        asleepAt = minute+1
    elif typeEntry == 'awake':
        for i in range(asleepAt, minute):
            guardAsleepMin[guard][i] += 1

maxCount = (0, None)
for gId, minutes in guardAsleepMin.items():
    count = sum(minutes.values())
    if count > maxCount[0]:
        maxCount = (count, gId)

maxMinCount = (0, None)
for minutes, count in guardAsleepMin[maxCount[1]].items():
    if count > maxMinCount[0]:
        maxMinCount = (count, minutes)


print("Guard {} slept for {} total minutes with the most minutes at {} minutes of midnight for {} minutes.".format(
    maxCount[1], maxCount[0], maxMinCount[1], maxMinCount[0]
    ))
print("mult: {}".format(maxCount[1]*maxMinCount[1]))