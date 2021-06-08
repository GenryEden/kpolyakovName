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

def check(x):
	for i in range(2, min(x, isqrt(x)+1)):
		if x % i == 0:
			return isSimple(x//i) and x//i != i

s = 0
cnt = 0
for x in range(351627, 428763):
	if check(x):
		cnt += 1
		s += x

print(cnt, floor(s/cnt))