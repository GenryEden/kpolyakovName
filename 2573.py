def getOddDels(x):
	for i in range(1, x+1, 2):
		if x % i == 0:
			yield i

for x in range(190061, 190072+1):
	dels = list(getOddDels(x))
	if len(dels) == 4:
		print(dels[-1], dels[-2])