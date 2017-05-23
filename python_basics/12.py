inp = [1,2,3,4,5,4,2,1,5,6,7,8,2,4,6]

d=dict()
for i in inp[:]:
	d[i]=d.get(i,0)+1

for k,v in d.items():
	print("Value %d occured %d time(s) in the list"%(k,v))	
