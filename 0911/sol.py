import sys
from collections import deque
sys.stdin = open('11725.txt')
n = int(input())
s = 0

tree = [ [] for _ in range(n+1)]

for _ in range(n-1): 
    a , b  = map(int,input().split())
    tree[a].append(b) #
    tree[b].append(a)

bfs = [0]*(n+1)
answer = deque()
def BFS(v):
    answer.append(v)
    bfs[v] = 1
    while answer: 
        now = answer.popleft()

        for to in tree[now]:
            if not bfs[to]:
                    bfs[to] = now
                    answer.append(to)


BFS(1)

for i in range(2,n+1):
    print(bfs[i])