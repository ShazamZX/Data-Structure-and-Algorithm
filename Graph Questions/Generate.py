#Create a graph in python
from collections import defaultdict
graph = defaultdict(list)
def addEdge(src,dst):
    global graph
    graph[src].append(dst)

#driver

addEdge('a','c')
addEdge('b','c')
addEdge('b','e')
addEdge('c','d')
addEdge('c','e')
addEdge('c','a')
addEdge('c','b')
addEdge('e','b')
addEdge('d','c')
addEdge('e','c')

print(graph)
