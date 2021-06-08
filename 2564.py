def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for x in range(194455, 194500):
	l = list(getDels(x))
	if len(l) == 4:
		print(l[-2], l[-1])