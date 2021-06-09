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

def check(x):
	for i in range(2, min(isqrt(x)+2, x)):
		if x % i == 0:
			if x//i != i and isSimple(x//i):
				return x//i, i
			else:
				return False
	return False

maxDist = 0
ans = [0,0]
for i in range(326359, 421986+1):
	res = check(i)
	if res:
		dist = res[0] - res[1]
		if dist > maxDist:
			maxDist = dist
			ans = res

print(*sorted(ans))