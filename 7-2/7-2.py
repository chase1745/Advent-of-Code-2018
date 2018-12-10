import sys
sys.path.append('..')
from adventHelper import FileReader
from collections import defaultdict
from operator import itemgetter

def format(line):
    line = line.split()
    return line[1], line[7]

def time(n):
    return ord(n) - 4

fr = FileReader(7, 2)

# Get graph
g = defaultdict(list)
gT = defaultdict(list)
for pre, step in map(lambda x:format(x), fr.getlines()):
    g[pre].append(step)
    gT[step].append(pre)

completed = set()
q = []

# Find starting Node
nodes = {n for n in g.keys()}
for nodeList in g.values():
    [nodes.remove(n) for n in nodeList if n in nodes]
q.extend(sorted(list(nodes))) # Starting nodes are only elements left

# Traverse graph
timeCount = 0
workers = [(None,0) for _ in range(5)]
while q or any(map(lambda x:x[0] is not None, workers)):
    # If q has any jobs not waiting on prerequisites
    if any(map(lambda node:all(map(lambda x:x in completed, gT[node])), q)): 
        for i in range(min(len(workers), len(q))):
            # Check for prereqs again in case after selecting one, all the remaining have prereqs
            if not any(map(lambda node:all(map(lambda x:x in completed, gT[node])), q)): break 
            if workers[i][0] is not None: continue
            # Make sure pre steps have been completed.
            node = q.pop(0)
            while not all(map(lambda x:x in completed, gT[node])):
                q.append(node)
                node = q.pop(0)
            # Good to go
            workers[i] = (node, time(node))

    for i in range(len(workers)):
        if workers[i][0] == None: continue
        workers[i] = (workers[i][0], workers[i][1] - 1)

        (node, currTime) = workers[i]
        if currTime == 0:
            completed.add(node)
            workers[i] = (None, 0)
            # Get neigbors
            for neighbor in g[node]:
                if neighbor not in completed and neighbor not in q and neighbor not in [n for (n, _) in workers]:
                    q.append(neighbor)

    timeCount += 1
    q = sorted(q)

print("Order for completion: {} with {} time.".format(''.join(list(completed)), timeCount))