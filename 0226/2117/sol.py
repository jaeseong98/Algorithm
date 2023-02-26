import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for tc in range(T):
    N,M = map(int(input().split()))
    arr = [list(map(int(input().split() for _ in range(N))))]

    for i in range(N):
        for j in range(N):
            res = 0
            if arr[i][j] == 1:
                ## 돌아야할 k 갯수
                r = min(i, j)
                for v in range(1,r+1):
                    cost = (v+1)**2 - (v)**2
                    ch = [[0] * for _ in range(N)]
                    dq = deque()
                    ch[i][j] = 1
                    dq.append((i, j))
                    for k
                    for k in range(4):
                        nx = i+dx[k]
                        ny = j+dy[k]
                        if 0<=nx<N and 0<=ny<N and ch[nx][ny] == 0:
                            dq.append((nx,ny))
                            ch[nx][ny] = 1
                            if arr[nx][ny] == 1:
                                cnt +=1




