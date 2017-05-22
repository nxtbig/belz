l = [int(x) for x in input().split()]
res = []
for i in l[:]:
	if i%5==0 and i!=0:
		res.append(i)
res.sort()
l = [str(x) for x in res[:]]
print(l)
#0 2 4 5 8 10 13 15 18 20 23 25 35 40 42 45       