#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

n,m = map(int,input().split())

answer = [0]*m

def backtracking(L,s):
    if L == m:
        for j in answer:
            print(j, end= " ")
        print()
        return
    for i in range(s,n+1):
        answer[L] = i
        backtracking(L+1,i)

backtracking(0,1)