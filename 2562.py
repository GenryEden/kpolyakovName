def getDels(x):
	for i in range(2, x):
		if x % i == 0:
			yield i

for x in range(174457, 174505+1):
	l = list(getDels(x))
	if len(l) == 2:
		print(*l)
