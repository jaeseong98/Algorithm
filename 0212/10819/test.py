a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

lst = list(map(list,zip(a,b,c)))


print(list(zip(*lst)))

t = [1,23,4,5,6,[1]]
print(*t)