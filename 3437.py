from math import isqrt
def getDels(x):
	dels = []
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			dels += [i, x//i]
	if isqrt(x)**2 == x:
		dels.remove(isqrt(x))
	return sorted(dels)

for x in range(862346, 1056242+1):
	dels = getDels(x)
	if len(dels) < 2:
		continue
	prev = dels[0]
	for i in dels[1:]:
		if i - prev != 100:
			break
	else:
		print(x, max(dels))