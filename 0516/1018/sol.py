#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

### Plan
#1.8*8의 반복문을 돌 수 있게 (n-8+1)까지 반복문 설정
#2.상하좌우의 좌표를 지정하여 만약 다른 값이 보인다면 cnt +=1 하고 다른 위치 xx의 값 변경
#3.cnt를 다 더했는데 mim_cnt보다 작다면 갱신
import copy
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]

# 상하좌우 좌표
dx = [-1,1,0,0]
dy = [0,0,-1,1]

horse = "WB"

new_board = copy.deepcopy(board)

min_cnt_1 = 1e+9
# 1번 작성
for a in range(n-7):
    for b in range(m-7):
        new_board = copy.deepcopy(board)
        cnt = 0
        # 체스판 반복
        for i in range(8):
            for j in range(8):
                now = new_board[a+i][b+j]
                other = horse.replace(now, "")
                # 2번 작성
                for k in range(len(dx)):
                    x = a+i+dx[k]
                    y = b+j+dy[k]
                    if a<=x<a+8 and b<=y<b+8:
                        if new_board[x][y] == now:
                            new_board[x][y] = other
                            cnt +=1
        print('min1', cnt)
        # 3번 작성
        min_cnt_1 = min(min_cnt_1,cnt)
def reverse_nested_lists(lst):
    reversed_lst = []
    for sublist in reversed(lst):
        if isinstance(sublist, list):
            reversed_lst.append(reverse_nested_lists(sublist))
        else:
            reversed_lst.append(sublist)
    return reversed_lst
#
reversed_board = reverse_nested_lists(board)
min_cnt_2 = 1e+9
# 1번 작성
for a in range(n-7):
    for b in range(m-7):
        new_board = copy.deepcopy(reversed_board)
        cnt = 0
        # 체스판 반복
        for i in range(a,a+8):
            for j in range(b,b+8):
                now = new_board[i][j]
                other = horse.replace(now, "")
                # 2번 작성
                for k in range(len(dx)):
                    x = i+dx[k]
                    y = j+dy[k]
                    if a<=x<a+8 and b<=y<b+8:
                        if new_board[x][y] == now:
                            new_board[x][y] = other
                            cnt +=1
        print('min2',cnt)
        # 3번 작성
        min_cnt_2 = min(min_cnt_2,cnt)


print(min(min_cnt_1,min_cnt_2))