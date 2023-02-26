import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        i, tree[i] = map(int, input().split())
    for j in range(N,1,-1):
        #홀수라면
        if j%2:
            v = (j-1)//2
            tree[v] += tree[j]
        else:
            v = j//2
            tree[v] += tree[j]
    print(f'#{tc} {tree[L]}')