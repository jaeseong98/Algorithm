import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ch = [0]*n
res = 1e9

# dfs
def dfs(L,idx):
    global res
    if L == n//2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if ch[i] and ch[j]:
                    start += arr[i][j]
                elif not ch[i] and not ch[j]:
                    link += arr[i][j]
        res = min(res , abs(start-link))
        return
    for i in range(idx,n):
        if not ch[i]:
            ch[i] = 1
            dfs(L+1,i+1)
            ch[i] = 0
dfs(0,0)
print(res)

