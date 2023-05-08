#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

n,k = map(int,input().split())

answer = 0
coin_list = []

# n번 반복
for i in range(n):
    coin_list.append(int(input()))

# 순서바꾸기
coin_list = coin_list[::-1]

for j in coin_list:
    if k//j:
        answer += k//j
        k = k%j
    else:
        pass

print(answer)