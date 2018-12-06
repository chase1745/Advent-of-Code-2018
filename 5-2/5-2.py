import string
import sys
sys.path.append('..')
from adventHelper import FileReader


def react(data):
    completed = False
    idxRemove = None
    while not completed:
        for i, c in enumerate(data):
            try:
                if abs(ord(c) - ord(data[i+1])) == 32:
                    idxRemove = i
                    break
            except:
                completed = True

        if not completed:
            data.pop(i+1)
            data.pop(i)

    return data

def removeLetter(data, letter):
    print(letter)
    idxs = []
    for i, c in enumerate(data):
        if c.lower() == letter: idxs.append(i)
    for i in reversed(idxs):
        data.pop(i)

    return data

fr = FileReader(5, 2)
data = react(list(fr.getfirstline().strip()))

print(min([len(react(removeLetter(list(data), c))) for c in string.ascii_lowercase]))