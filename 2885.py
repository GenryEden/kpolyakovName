from math import isqrt
def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, isqrt(x)+1, 2):
		if x % i == 0:
			return False
	return True

maximal = 0
cnt = 0

for i in range(int(125873**0.25)-2, int(136762**0.25)+2):
	x = i**4
	if 125873 <= x <= 136762 and isSimple(i):
		cnt += 1
		maximal = x

print(cnt, maximal)