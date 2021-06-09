from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+1), 2):
		if x % i == 0:
			return False
	return True

def check(x):
	for i in range(2, min(x, isqrt(x) + 1)):
		if x % i == 0:
			return x//i != i and isSimple(x//i)
	return False

ans = 0
for i in range(3594, 21891+1):
	if check(i):
		ans = i

print(ans)