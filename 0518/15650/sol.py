#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

n,m = map(int,input().split())

answer = [0]*m
def backtracking(L,s):

    # 길이가 m이라면 출력
    if L == m:
        for j in answer:
            print(j,end = " ")
        print()
        return
    # s부터 n+1까지 반복문
    for i in range(s,n+1):
        answer[L] = i  # answer의 인덱스 위치에 i 넣기
        backtracking(L+1, i+1)


backtracking(0,1)



