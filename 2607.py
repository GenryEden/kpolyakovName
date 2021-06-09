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
			return (x//i != i) and (i % 10 == (x//i) % 10) and isSimple(x//i)

cnt = 0
minimal = 0
for i in range(173225, 217437):
	if check(i):
		cnt += 1
		if cnt == 1:
			minimal = i
print(cnt, minimal)