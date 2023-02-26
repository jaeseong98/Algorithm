import sys
sys.stdin = open('input.txt')

def check1(i,j):
    cnt = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt += arr[i][j]
    for v in range(1,M):
        for k in range(4):
            nx = i+dx[k]*v
            ny = j+dy[k]*v
            if 0<=nx<N and 0<=ny<N:
                cnt += arr[nx][ny]
    return cnt
def check2(i,j):
    cnt = 0
    dx = [-1,1,-1,1]
    dy = [1,1,-1,-1]
    cnt += arr[i][j]
    for v in range(1,M):
        for k in range(4):
            nx = i+dx[k]*v
            ny = j+dy[k]*v
            if 0<=nx<N and 0<=ny<N:
                cnt += arr[nx][ny]
    return cnt
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(N):
            res = max(check1(i,j),res,check2(i,j))
    print(f'#{tc} {res}')