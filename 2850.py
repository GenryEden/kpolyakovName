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

def check(x):
	for i in range(2, min(x, isqrt(x)+2)):
		if x % i == 0:
			if x//i != i and isSimple(x//i):
				return x//i - i
			else:
				return False
	return False

cnt = 0
maxDist = 0
ans = 0

for x in range(356738, 404321+1):
	res = check(x)
	if res:
		cnt += 1
		if res > maxDist:
			maxDist = res
			ans = x

print(cnt, ans)