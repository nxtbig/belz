l = [1,'a',['d','e','f'],2,-1,(1,2,3),'g']

l = filter(lambda x: type(x) is int, l)
print l