import sys
sys.stdin = open('input.txt')

num_dict = {'0':'0001101',
            '1':'0011001',
            '2':'0010011',
            '3':'0111101',
            '4':'0100011',
            '5':'0110001',
            '6':'0101111',
            '7':'0111011',
            '8':'0110111',
            '9':'0001011'}
T = int(input())

def check(num):
    ans = 0
    for i in range(0,8,2):
        ans += int(num[i])
    ans *=3
    for j in range(1,9,2):
        ans += int(num[j])
    print(num,ans)
    if not ans%10:
        return sum(list(map(int,num)))
    else:
        return 0

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    for a in arr:
        for i,j in num_dict.items():
            a = a.replace(j,i)
        if int(a) != 0:
            res = str(int(a))[:8]
            break
    print(check(res))
