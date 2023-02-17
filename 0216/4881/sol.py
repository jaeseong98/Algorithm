import sys
sys.stdin = open('input.txt')

tc = int(input())
def dfs(L):
    global min_value
    if L == n:
        new_r = list(zip(res,r))
        hap = 0
        for x,y in new_r:
            hap += arr[x][y]
            if hap>=min_value:
                break

        min_value = min(hap,min_value)
        return
    for i in range(1,n+1):
        if ch[i] == 0:
            ch[i] = 1
            res[L] = r[i-1]
            dfs(L+1)
            ch[i] = 0

for i in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ch = [0] * (n + 1)
    res = [0] * n
    r = list(range(n))
    min_value = 1e9

    dfs(0)
    print(f"#{i+1} {min_value}")



