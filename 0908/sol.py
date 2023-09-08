import sys
from collections import deque

sys.stdin = open("input.txt")

dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int,input().split()))for _ in range(h)]
    cnt = 0
    dq = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dq.append((i,j))
                cnt +=1
                while dq:
                    x,y = dq.pop()
                    arr[x][y] = 0
                    for k in range(len(dx)):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0<=nx<h and 0<=ny<w:
                            if arr[nx][ny] == 1:
                                dq.append((nx,ny))
                                arr[nx][ny] = 0
    print(cnt)


# BFS로 탐색해서 군집갯수 찾기
# DFS였다면 popleft()


