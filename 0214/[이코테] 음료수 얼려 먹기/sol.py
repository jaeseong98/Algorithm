import sys

sys.stdin = open('input.txt')

n,m = map(int,input().split())

board = [list(map(int,input())) for _ in range(n)]
print(board)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = []
def dfs(x,y):
    global cnt
    board[x][y] = 1
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<n and 0<=yy<m and board[xx][yy] == 0:
            board[xx][yy] = 1
            dfs(xx,yy)



for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt = 0
            dfs(i,j)
            res.append(cnt)

print(len(res))

