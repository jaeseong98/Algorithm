import sys
from collections import deque
import copy
sys.stdin = open('input.txt')

n,m = map(int,input().split())

board = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ch = copy.deepcopy(board)
res = []
dq = deque()
dq.append((0,0))
def bfs():
    while dq:
        x,y = dq.popleft()
        ch[x][y] = 0
        if (x,y) == (n-1,m-1) :
            print(board[x][y]-1)
            break

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and ch[nx][ny] == 1:
                ch[nx][ny] = 0
                board[nx][ny] = board[x][y] +1
                dq.append((nx,ny))
bfs()
