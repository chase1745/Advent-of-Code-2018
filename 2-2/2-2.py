import sys
sys.path.append('..')
from adventHelper import FileReader

def similar(l1, l2):
    for i in range(len(l1)):
        if l1[:i]+l1[i+1:] == l2[:i]+l2[i+1:]:
            return True, l1[:i]+l1[i+1:]
    return False, None

fr = FileReader(2, 2)

lines = [l.strip() for l in fr.getlines()]

found = False
for l1 in lines:
    if found: break
    for l2 in lines:
        if l1 == l2: continue
        sim, val = similar(l1, l2)
        if sim:
            found = True
            break
print("Common string: " + val)