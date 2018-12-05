import sys
sys.path.append('..')
from adventHelper import FileReader
from collections import defaultdict
import re
import operator


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

fr = FileReader(4, 2)
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

maxMinutes = (0, None, None)
for gId, minutes in guardAsleepMin.items():
    (currMaxMinutes, currMaxCount) = max(minutes.items(), key=operator.itemgetter(1))
    if currMaxCount > maxMinutes[0]:
        maxMinutes = (currMaxCount, currMaxMinutes, gId)

print("Guard {} was most frequently asleep at minute {}".format(maxMinutes[2], maxMinutes[1]))
print("Mult: {}".format(maxMinutes[2]*maxMinutes[1]))