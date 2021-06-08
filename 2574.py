def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for x in range(11275, 16328):
	dels = list(getDels(x))
	if len(dels) == 5:
		print(dels[-3], dels[-2])