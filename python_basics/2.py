l = [int(x) for x in input().split()]
res = []
for i in l[:]:
	if i%5==0 and i!=0:
		res.append(i)
res.sort()
print(res)