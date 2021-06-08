def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for i in range(int(652938**0.25)-5, int(1744328**0.25)+5):
	x = i**4
	if 652938 <= x <= 1744328:
		dels = list(getDels(x))
		if len(dels) == 5:
			print(dels[-3], dels[-2])