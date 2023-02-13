import sys

sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

rg = list(range(n))
ch = [0]*(n+1)
res = [0]*n
ans = 1e9
total = 0
for i in range(n):
    for j in range(n):
        total += arr[i][j]
def dfs(L,s):

    global ans,cnt
    if L == n//2:
        start_score = 0
        link_score = 0
        start_team = res[:n//2]
        link_team = list(set(range(n)) - set(start_team))
        print(start_team,link_team)
        # 이중리스트를 돌면 모든 i,j의 경우의 수를 구할 수 있음 com(list,2)느낌
        for i in range(n//2):
            for j in range(i+1,n//2):
                x,y = start_team[i],start_team[j]
                w,z = link_team[i],link_team[j]
                start_score += arr[x][y] + arr[y][x]
                link_score += arr[w][z] + arr[z][w]
        ans = min(ans,abs(start_score - link_score))
        return
    for i in range(s,n+1):
        res[L] = rg[i-1]
        dfs(L+1,i+1)
dfs(0,1)
print(ans)
