from math import isqrt, floor

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
			if x//i != i and ((x//i) % 10 == i % 10) and isSimple(x//i):
				return i, x//i
			else:
				return False
	return False

def check(x):
	for i in range(2, min(x, isqrt(x)+2)):
		if x % i == 0:
			res = check2(x//i)
			return bool(res) and (i not in res) and (i % 10 == res[0] % 10)
	return False
cnt = 0
s = 0
for i in range(356712, 420901):
	if check(i):
		cnt += 1
		s += i

print(cnt, floor(s/cnt))