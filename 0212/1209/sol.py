import sys
sys.stdin = open('input.txt')



def solve(arr):
    col_sum = [0 for _ in range(len(arr))]
    ans = 0
    a_sum = 0
    b_sum = 0
    for i in range(len(arr)):
        ans = max(ans,sum(arr[i]))
        a_sum += arr[i][i]
        b_sum += arr[i][len(arr) - i - 1]
        for j in range(len(arr)):
            col_sum[i] += arr[j][i]


    col_max = max(col_sum)
    ans = max(ans,col_max,a_sum,b_sum)
    return ans


for _ in range(10):
    tc = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]
    print(f'#{tc}', solve(array))

