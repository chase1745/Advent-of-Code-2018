import sys
sys.path.append('..')
from adventHelper import FileReader
from collections import defaultdict

def format(line):
    line = line.split()
    return line[1], line[7]

fr = FileReader(7, 1)

# Get graph
g = defaultdict(list)
gT = defaultdict(list)
for pre, step in map(lambda x:format(x), fr.getlines()):
    g[pre].append(step)
    gT[step].append(pre)

completed = []
q = []

# Find starting Node
nodes = {n for n in g.keys()}
for nodeList in g.values():
    [nodes.remove(n) for n in nodeList if n in nodes]
q.extend(sorted(list(nodes))) # Starting nodes are only elements left

# Traverse graph
i = 0
while q:
    node = q.pop(0)

    # Make sure pre steps have been completed.
    if not all(map(lambda x:x in completed, gT[node])):
        q.append(node)
        i += 1
        continue
    # Good to go
    completed.append(node)

    # Get neigbors
    for neighbor in g[node]:
        if neighbor not in completed and neighbor not in q:
            q.append(neighbor)
    q = sorted(q)
    i = 0

print("Order for completion: {}".format(''.join(completed)))