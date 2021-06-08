def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for i in range(135743, 135789):
	dels = list(getDels(i))
	if len(dels) == 6:
		print(dels[-2], dels[-1])