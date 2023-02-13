import sys

sys.stdin = open('input.txt')

n = int(input())


def check(arr):
    for i in range(1,len(arr)//2+1):
        if arr[-i:] == arr[-(i*2):-i]:
            return False
    return True
def dfs(arr):
    if len(arr) == n:
        print(arr)
        exit()
    for i in '123':
        ## 좋은수열이라면
        if check(arr+i):
            ## 3개다 좋은수열이 안딘다면 하나 빠진 arr에서 다시시작한다 그때는 앞에 숫자 다음걸로
            dfs(arr+i)


dfs('')