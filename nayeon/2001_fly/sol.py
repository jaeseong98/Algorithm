import sys
sys.stdin = open('input.txt')

T = int(input())
    for
    N, M  = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]


dx = list(range(m))*m
dy = sorted(dx)
max_value = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        sum = 0
        for k in range(len(dx)):
            sum += arr[i+k][j+k]
        if sum >= max_value:
            max_value = sum
print(max_value)



