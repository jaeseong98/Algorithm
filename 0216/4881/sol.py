import sys
sys.stdin = open('input.txt')

tc = int(input())
def dfs(L,sum):
    global min_value
    if L == n:
        if sum <= min_value:
            min_value = sum
            return
    elif sum > min_value:
        return
    for i in range(0,n):
        if ch[i] == 0:
            ch[i] = 1
            dfs(L+1,sum+arr[L][i])
            ch[i] = 0

for i in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ch = [0] * (n + 1)
    res = [0] * n
    r = list(range(n))
    min_value = 1e9

    dfs(0,0)
    print(f"#{i+1} {min_value}")



