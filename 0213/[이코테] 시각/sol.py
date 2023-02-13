import sys

sys.stdin = open('input.txt')

n = int(input())

three_count = 0

for i in range(60):
    if '3' in str(i):
        three_count +=1

not_three_count = 60 - three_count

h_count = 0
for i in range(n):
    if '3' in str(i):
        h_count +=1

total = (n+1)*60*60
minus = (n+1-h_count)*not_three_count*not_three_count
print(total-minus)