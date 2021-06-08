from math import isqrt

def getDels(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield i


for i in range(int(244143**0.25)-3, int(1367821**0.25)+3):
	x = i**4
	if 244143 <= x <= 1367821:
		dels = list(getDels(x))
		if len(dels) == 5:
			print(dels[-3], dels[-2])