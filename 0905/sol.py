import sys

sys.stdin = open('input.txt')

n = int(input())

maraton = []

for _ in range(n):
    name = input()
    
    maraton.append(name)
    

for _ in range(n-1):
    
    clear = input()
    maraton.append(clear)

from collections import Counter

cnt = Counter(maraton)


for key,values in cnt.items():
    if values%2:
        print(key)
        break
