def listflat(inp):
	for i in inp:
		if type(i) is list:
			listflat(i)
		else:
			out.append(i)

inp = [[1,2,3],[4,5],[6,7,8]]
out = []

listflat(inp)
print(out)