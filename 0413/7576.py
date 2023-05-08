import sys
sys.stdin = open('input.txt')

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

from copy import deepcopy
arr2 = deepcopy(arr)

from collections import deque
arr2 = deepcopy(arr)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dq = deque()

result = []
zero_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            dq.append((i,j))
        if arr[i][j] == 0:
            zero_cnt +=1

if zero_cnt == 0:
    print(0)
else:
    answer = 0
    while dq:
        size = len(dq)
        for i in range(size):
            x,y = dq.popleft()
            for k in range(len(dx)):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0<=xx<n and 0<=yy<m:
                    if arr2[xx][yy] == 0:
                        arr2[xx][yy] = 1
                        dq.append((xx,yy))
        if dq:
            answer += 1


    zero = 0
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 0:
                zero+=1
    if zero:
        print(-1)
    else:
        print(answer)


