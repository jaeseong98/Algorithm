#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

#리스트 생성
city_num = int(input())
liter_lst = list(map(int,input().split()))
cost_lst = list(map(int,input().split()))

#처음 시작 비용 설정
min_liter = cost_lst[0]

answer = 0

#휴게소에서 더 작은 코인(비용)이 생기면 갱신 아니면 기존 비용으로 계산
for coin,liter in zip(cost_lst[:-1],liter_lst):
    if coin <= min_liter:
        min_liter = coin
        answer += min_liter*liter
    else:
        answer += min_liter*liter
print(answer)