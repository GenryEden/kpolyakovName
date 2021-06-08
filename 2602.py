from math import isqrt

def isSimple(x):
	if x == 1:
		return False
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, min(x, isqrt(x)+1), 2):
		if x % i == 0:
			return False
	return True

def check(x):
	for i in range(2, min(isqrt(x)+1, x)):
		if x % i == 0:
			return isSimple(x//i) and x//i != i
toAns = []
for x in range(412567, 473265+1):
	if check(x):
		toAns.append(x)
mid = sum(toAns)/len(toAns)
toAns.sort(key=lambda x: abs(x-mid))
print(len(toAns), toAns[0])