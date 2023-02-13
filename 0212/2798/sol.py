import sys
sys.stdin = open('input.txt')

n,m = map(int,input().split())
arr = list(map(int,input().split()))

res = [0]*4
ch = [0]*(n+1)
ans = 0

def dfs(L,sum):
    global ans
    if L == 3:
        if ans<= sum <=m:
            ans = sum
        return
    for i in range(1,n+1):
        if ch[i] == 0:
            ch[i] = 1
            res[L] = arr[i-1]
            dfs(L+1,sum+arr[i-1])
            ch[i] = 0 #조합일 경우 안풀어줘도 됨
dfs(0,0)
print(ans)


