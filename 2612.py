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
			if x//i != i and ((x//i) % 10 == i % 10) and isSimple(x//i):
				return x//i, i
			else:
				return False
	return False

def check(x):
	for i in range(2, min(x, isqrt(x)+1)):
		if x % i == 0:
			res = check2(x//i)
			if res and (i not in res) and i % 10 == res[0] % 10:
				res = list(res) + [i]
				return max(res) - min(res)
			else:
				return False
	return False

cnt = 0
maxDist = 0
ans = 0

for i in range(536792, 604298+1):
	res = check(i)
	if res:
		cnt += 1
		if res > maxDist:
			maxDist = res
			ans = i

print(cnt, ans)