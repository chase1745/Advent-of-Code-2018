import sys
sys.path.append('..')
from adventHelper import FileReader

fr = FileReader(5, 1)
data = list(fr.getfirstline().strip())

completed = False
idxRemove = None
while not completed:
    for i, c1 in enumerate(data):
        try:
            if abs(ord(c1) - ord(data[i+1])) == 32:
                idxRemove = i
                break
        except:
            completed = True
    if not completed:
        data.pop(i+1)
        data.pop(i)

print(len(data))


