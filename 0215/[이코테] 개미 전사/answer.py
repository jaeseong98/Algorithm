import sys

sys.stdin = open('input.txt')

n = int(input())

arr = list(map(int,input().split()))

# 앞서 계산된 결과를 저장하기 위해 DP테이블 초기화
d = [0]*100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])

print(d[n-1])