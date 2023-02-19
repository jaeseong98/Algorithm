import sys

sys.stdin = open('input.txt')

T = int(input())
dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(len(dx)):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<n and 0<=ny<m and arr[nx][ny] < arr[i][j]:
                    cnt +=1
            if cnt >=4:
                res +=1

    print(f'#{tc} {res}')


