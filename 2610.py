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

def check2(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			if isSimple(x//i) and i != x//i:
				return i, x//i
			else:
				return False
	return False

def check(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			res = check2(x//i)
			return res and (i not in res)
	return False

cnt = 0
maximal = 0
for i in range(105673, 220784+1):
	if check(i):
		cnt += 1
		maximal = i

print(cnt, maximal)