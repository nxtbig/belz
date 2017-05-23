keys=['team1','teamX','team4','team5']
inp = {'team1':'Alpha', 'team2':'Beta', 'team3':'Gamma', 'team4':'Delta'}
out={}
for k in keys[:]:
	val = inp.get(k,'none')
	if val!='none':
		out[k]=val
print(out)