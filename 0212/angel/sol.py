import sys

sys.stdin = open('input.txt')
def solve(total_page,pa,pb):
    lt = 1
    rt = total_page
    def check(lt, rt, goal):
        cnt = 1
        while True:
            mid = (lt + rt) // 2
            if mid == goal:
                return cnt
            if mid > goal:
                rt = mid
                cnt += 1
            elif mid < goal:
                lt = mid
                cnt += 1


    ans_pa = check(lt, rt, pa)
    ans_pb = check(lt, rt, pb)
    if ans_pa < ans_pb:
        return 'A'
    elif ans_pa > ans_pb:
        return 'B'
    else:
        return 0


n = int(input())
for i in range(n):
    total_page,pa,pb = map(int,input().split())
    print(f'#{i+1}',solve(total_page,pa,pb))

