print('Enter list of words')
l1 = input().split()

print('Enter n')
n=int(input())

res = []
for i in l1[:]:
	if len(i)>n:
		res.append(i)
res.sort()
print(res)