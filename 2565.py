def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for x in range(154026, 154043+1):
	dels = list(getDels(x))
	if len(dels) == 4:
		print(dels[-2], dels[-1])
