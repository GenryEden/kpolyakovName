def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i

for i in range(int(1820348**0.25)-5, int(2880927**0.25)+5):
	x = i**4
	if 1820348 <= x <= 2880927:
		dels = list(getDels(x))
		if len(dels) == 5:
			print(dels[-2], dels[-1])