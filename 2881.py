from math import isqrt
def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(isqrt(x)+1, x), 2):
		if x % i == 0:
			return False
	return True

cnt = 0
for x in reversed(range(2532000, 2532160)):
	if isSimple(x):
		cnt += 1
		print(cnt, x)
	