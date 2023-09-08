import sys
from collections import deque

sys.stdin = open('2644.txt')
INF = int(1e9)

n = int(input())

a,b = map(int,input().split())

m = int(input())

graph = [[] for _ in range(n+1)]


# distance = [INF]*(n+1)
visited = [False]*(n+1)

for _ in range(m):
    p,c = map(int,input().split())
    graph[p].append(c)
    graph[c].append(p)

dq = deque()

def min_distance(start,end):
    visited[start] = True
    dq.append((start,0)) # 현재 노드와 거리, 이때 거리간격은 계속 1
    while dq:
        node , distance = dq.popleft()
        print(node,distance)
        if node == end :
            return distance
        # now = dq.popleft()
        visited[node] = True
        for to in graph[node]:
            if not visited[to] :
                dq.append((to,distance + 1))
    return -1

result = min_distance(a,b)
print(result)


