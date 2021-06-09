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
			return (x//i != i) and ((x//i) % 10 == i % 10) and isSimple(x//i)

cnt = 0
maximal = 0

for i in range(237981, 309876+1):
	if check(i):
		cnt += 1
		maximal = i

print(cnt, maximal)