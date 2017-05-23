from calendar import monthrange

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def schedule(month):

	v = monthrange(2017,months.index(month)+1)
	day = v[0]
	for i in range(1,v[1]+1):
		if days[day]=='Sunday':
			print("On %d, %s 2016 (%s): All cars are allowed"%(i,month,days[day]))
		elif i%2==0:
			print("On %d, %s 2016 (%s): Even cars are allowed"%(i,month,days[day]))
		else:
			print("On %d, %s 2016 (%s): Odd cars are allowed"%(i,month,days[day]))
		day=(day+1)%7

schedule('May')