from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			return False
	return True

def check2(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			if x//i != i and (x//i) % 10 == i % 10 and isSimple(x//i):
				return i, x//i
			else:
				return False
	return False

def check(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			res = check2(x//i)
			if res and (i not in res) and i % 10 == res[0] % 10:
				return res[1] - i
			else:
				return False
	return False

cnt = 0
minDist = float('inf')
ans = 0
for i in range(485617, 529678+1):
	res = check(i)
	if res:
		cnt += 1
		if res < minDist:
			minDist = res
			ans = i

print(cnt, ans)