#백준 제출시 삭제
import sys
sys.stdin = open('input.txt')

sik = input()

# 마이너스 부호로 split
sik = sik.split('-')

# 쪼개진 식들을 연산후 리스트에 넣기
answer = []
for i in sik:
    # +로 묶였을 경우 쪼개주고 리스트로 구분 -> sum해서 한번에 계산, 단독이라면 그냥 sum
    res = list(map(int, i.split('+')))
    answer.append(str(sum(res)))

# 최종 리스트를 "-"로 조인후 다시 eval
print(eval("-".join(answer)))



