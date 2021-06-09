from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+2), 2):
		if x % i == 0:
			return False
	return True

def check2(x):
	for i in range(2, min(x, isqrt(x)+2)):
		if x % i == 0:
			if x//i != i and isSimple(x//i):
				return i, x//i
			else:
				return False
	return False

def check(x):
	for i in range(2, min(x, isqrt(x)+2)):
		if x % i == 0:
			res = check2(x//i)
			return res and (i not in res)
	return False


cnt = 0
minimal = 0

for i in range(158928, 345293+1):
	if check(i):
		cnt += 1
		if cnt == 1:
			minimal = i

print(cnt, minimal)