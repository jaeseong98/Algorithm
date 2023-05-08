#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

n = int(input())


room = []

for _ in range(n):
    room.append(list(map(int,input().split())))

# 회의 종료시간으로 정렬 이후 시작시간으로 정렬(같은 시각에 종료하는데 시작시간이 빠른것이 먼저 오기위해
room.sort(key = lambda x : (x[1],x[0]))


# 첫번째 회의실은 끝나는 시간이 제일 작은 회의실로 고정
time = room[0][1]
answer = 1

# 다음 회의실의 시간시간이 현재 종료시간보다 크다면 회의실 선택(이미 정렬했기때문에)
for start,end in room[1:]:
    if end >= time and start >= time:
        time = end
        answer += 1
print(answer)
