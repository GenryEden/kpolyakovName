from math import isqrt

def isSimple(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			return False
	return True

cnt = 0
for x in range(2532000, 2532160+1):
	if isSimple(x):
		cnt += 1
		print(cnt, x)
		if cnt == 5:
			break