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

cnt = 0

for i in range(int(20789**0.25)-2, int(35672**0.25)+2):
	x = i**4
	if 20789 <= x <= 35672 and isSimple(i):
		cnt += 1
		if cnt == 1:
			minimal = x
print(cnt, minimal)