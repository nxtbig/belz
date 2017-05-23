region = 'RINA'
val = None

d = dict()
d['RINA']='Region India'
d['RMEA']='Region Middle East'
d['RSSA']='Region Sub-Saharan Africa'
d['RNEA']='Region North East Asia'
d['RASO']='Region South East Asia & Oceania'

print("Region '%s' stands for '%s'"%(region, d.get(region, 'Unknown')))