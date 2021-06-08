from math import isqrt

def isSimple(x):
	if x <= 1:
		return False
	elif x == 2:
		return True
	elif x % 2 == 0:
		return False
	for i in range(3, isqrt(x)+2, 2):
		if x % i == 0:
			return False
	return True

cnt = 1
for i in range(3532000, 3532160):
	if isSimple(i):
		print(cnt, i)
		cnt += 1