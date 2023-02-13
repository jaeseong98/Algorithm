import sys

sys.stdin = open('input.txt')

loc = input()

alp = ['a','b','c','d','e','f','g','h']

x = int(loc[1])
y = alp.index(loc[0])+1

dx = [-2,-2,2,2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

cnt = 0
for k in range(len(dx)):
    nx = x+dx[k]
    ny = y+dy[k]
    if 0<nx<=8 and 0<ny<=8:
        cnt +=1
print(cnt)