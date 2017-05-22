x = input().split()
n = int(input())
for k,v in enumerate(x):
	x[k] = v[:n]+v[n+1:]
print(x)