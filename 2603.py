from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(isqrt(x)+1, x)):
		if x % i == 0:
			return False
	return True

def check(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			if isSimple(x//i) and x//i != i:
				return x//i - i
			else:
				return False

ans = 0
minDist = float('inf')
for x in range(523456, 578925):
	res = check(x)
	if res:
		if minDist > res:
			minDist = res
			ans = x

for i in range(2, ans):
	if ans % i == 0:
		print(i, ans//i)
		break
