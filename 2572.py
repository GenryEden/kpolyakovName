def getEvenDels(x):
	for i in range(2, x+1, 2):
		if x % i == 0:
			yield i


for x in range(190201, 190260):
	dels = list(getEvenDels(x))
	if len(dels) == 4:
		print(dels[-1], dels[-2])