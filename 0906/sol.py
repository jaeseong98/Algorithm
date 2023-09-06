import sys

sys.stdin = open('input.txt')

from collections import Counter
# 1. 빈도수
# 2. 길이
# 3. 사전 순
# 4. m이상

n,m = map(int,input().split())

answer = []
for _ in range(n):
    name = input()
    if len(name)>=m:
        answer.append(name)

answer = Counter(answer)
answer  = sorted(answer.items(), key = lambda x : x[0])
answer = sorted(answer, key = lambda x : (x[1],len(x[0])),reverse = True)

print(answer)
for i in answer:
    print(i[0])