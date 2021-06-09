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
minDist = float('inf')
ans = 0

for i in range(478392, 502439+1):
	res = check(i)
	if res:
		cnt += 1
		if res < minDist:
			minDist = res
			ans = i

print(cnt, ans)