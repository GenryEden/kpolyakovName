def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for x in range(180131, 180179):
	dels = list(getDels(x))
	if len(dels) == 6:
		print(dels[-2], dels[-1])