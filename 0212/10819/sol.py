import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))

def cal(lst):
    sum = 0
    for i in range(0,len(lst)-1):
        sum += abs(lst[i]-lst[i+1])
    return sum

ch = [0]*(N+1)
res = [0]*N
ans = 0

##모든 경우의 수 dfs로 만들기
def dfs(L,arr):
    global ans
    if L == N:
        print(res)
        ans = max(ans,cal(res))
    for i in range(1,N+1):
        if ch[i] == 0:
            ch[i] = 1
            res[L] = arr[i-1]
            dfs(L+1,arr)
            ch[i] = 0
dfs(0,arr)
print(ans)



