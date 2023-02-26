import sys
sys.stdin = open('input.txt')


T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def count(x,y):
    cnt = 0
    cnt += arr[x][y]
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            cnt += arr[nx][ny]
    return cnt

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(M):
            res = max(count(i,j),res)
    print(f'#{tc} {res}')

