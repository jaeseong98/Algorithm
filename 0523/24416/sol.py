#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

n = int(input())
fib_cnt = 0
fibonacci_cnt = 0
def fib(n):
    global fib_cnt
    if n==1 or n==2:
        fib_cnt += 1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global fibonacci_cnt
    # f[1], f[2] 둘다 1로 시작하므로 모든 값을 1로 설정 이후 값들은 피보나치로 더해짐
    f = [1]*(n+1)
    for i in range(3,n+1):
        f[i] = f[i-1]+f[i-2]
        fibonacci_cnt += 1
    return f[n]

# 파이썬으로 피보나치 n 40을 돌면 시간초과가 남
fibonacci(n)
print(fib(n),fibonacci_cnt)