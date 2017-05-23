l = [1,'a',['d','e','f'],2,-1,(1,2,3),'g']
out=[]
for i in l:
	if type(i) is int:
		out.append(i)
print(out)