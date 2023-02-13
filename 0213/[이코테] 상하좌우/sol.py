import sys

sys.stdin = open('input.txt')

n = int(input())
arr = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']
x,y = 1,1
for plan in arr:

    for k in range(len(move)):
        if plan == move[k]:
            nx = x +dx[k]
            ny = y +dy[k]
    if 0<nx<=5 and 0<ny<=5:
        x,y = nx,ny
print(x,y)


