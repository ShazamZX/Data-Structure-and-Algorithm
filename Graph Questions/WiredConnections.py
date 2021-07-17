#There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 

from collections import defaultdict

def dfs(graph,node,visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph,neighbor,visited)


def make_connections(n,connections):
    if len(connections) < n-1:
        return -1
    graph = defaultdict(list)
    for node in range(n):
        graph[node] = []
    #creating adjacency list
    for node in connections:
        u,v = node[0],node[1]
        graph[u].append(v)
        graph[v].append(u)

    ans = 0
    
    visited = [False for _ in range(n)]
    for node in graph:
        if not visited[node]:
            ans+=1
            dfs(graph,node,visited)
    
    return ans-1


#driver code

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(make_connections(n,connections))

