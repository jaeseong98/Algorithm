import sys
sys.stdin = open('input.txt')

def check():
    ## 가로줄 확인
    for lst in arr:
        cnt = 0
        for num in lst:
            if num == 1:
                cnt +=1
                if cnt >=5:
                    return 1
            else:
                cnt = 0
    return 0
def check2():
    ## 세로줄 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt +=1
                if cnt >= 5:
                    return 1
            else:
                cnt = 0
    return 0

def check3(x,y):
    dx = [-2,2,1,-1]
    dy = [-2,2,1,-1]
    cnt = 1
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            cnt += arr[nx][ny]
    if cnt >=5:
        return 1
    else:
        return 0
def check4(x,y):
    dx = [2,-2,-1,1]
    dy = [-2,2,1,-1]
    cnt = 1
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            cnt += arr[nx][ny]
    if cnt >=5:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().replace("o","1").replace(".","0")))for _ in range(N)]
    if check() or check2():
        print("YES.1")
        continue
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                if check3() or check4():
                    print("YES.2")
                    break
    else:
        print("NO")
