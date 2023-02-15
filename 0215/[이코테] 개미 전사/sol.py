import sys

sys.stdin = open('input.txt')

n = int(input())

arr = list(map(int,input().split()))

max = 0
for i in range(n-2):
    value = arr[i]
    for j in range(i+2,n):
        if max <= value+arr[j]:
            max = value+arr[j]
print(max)