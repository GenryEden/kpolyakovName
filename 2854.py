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
			return x//i != i and isSimple(x//i)
	return False

toAns = []

for i in range(298435, 363249+1):
	if check(i):
		toAns.append(i)
mid = sum(toAns)/len(toAns)
toAns.sort(key=lambda x: abs(x-mid))
print(len(toAns), toAns[0])