import sys

sys.stdin = open('input.txt')

n,m = map(int,input().split())

arr = list(map(int,input().split()))

def check(h):
    sum  = 0
    for i in arr:
        if i>h:
            sum += i-h
    return sum
result = 0
def solve():
    global result
    s = 1
    e = max(arr)
    mid = (s + e) // 2
    while s<=e:
        mid = (s + e) // 2
        ans = check(mid)
        if ans>=m:
            s = mid + 1
            result = mid
        else:
            e = mid - 1


solve()
print(result)
