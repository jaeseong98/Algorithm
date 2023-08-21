num = int(input())
s = input()

s_list = []
answer = []

# if num == 3:
# 	print(6)
# else:
for i in range(1,num-1):
	answer.append(s[:i]) # 첫번째 문자열
	for j in range(1,num-i): # 두번째부터 1~num-i번째까지 늘리면서 두번째(중간 문자열 생성)
		answer.append(s[i:i+j]) # 두번째 문자열 
		answer.append(s[i+j:])  # 세번째 문자열은 나머지 자동
		s_list.append((s[:i],s[i:i+j],s[i+j:]))
answer = sorted(set(answer)) # 중복제거(set) , 정렬(sorted)

res = 0
for a,b,c in s_list: # 정렬된 문자열에서 위치 찾아서 인덱스 값으로 max 갱신
	idx_a = answer.index(a) + 1 
	idx_b = answer.index(b) + 1
	idx_c = answer.index(c) + 1
	res = max(idx_a+idx_b+idx_c,res)
print(res)