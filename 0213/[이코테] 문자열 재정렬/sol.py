import sys

sys.stdin = open('input.txt')

s = input()

string = ''
num = 0

for i in s:
    if i.isdecimal():
        num += int(i)
    else:
        string += i
answer = "".join(sorted(list(string)))
print(answer+ str(num))