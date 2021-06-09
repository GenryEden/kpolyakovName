from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(isqrt(x)+2, x), 2):
		if x % i == 0:
			return False
	return True

def check2(x, d=False):
	for i in range(2, min(x, isqrt(x)+2)):
		if x % i == 0:
			if d:
				print(i, x//i)
			if x//i != i and (x//i % 10 == i % 10) and isSimple(x//i):
				return i, x//i
			else:
				return False

	return False

def check(x, d=False):
	for i in range(2, min(x, isqrt(x)+2)):
		if x % i == 0:
			res = check2(x//i, d=d)
			if d:
				print(res, i)
			return res and (i not in res) and (i % 10 == res[0] % 10)
	return False

cnt = 0
minimal = 0
for x in range(318216, 369453+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal)