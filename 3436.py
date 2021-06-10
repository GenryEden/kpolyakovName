from math import isqrt

def getDels(x):
	dels = []
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			dels += [x//i, i]
	if isqrt(x)**2 == x:
		dels.remove(isqrt(x))

	return sorted(dels)

for i in range(834567, 1143210+1):
	dels = getDels(i)
	if len(dels) == 0 or len(dels) == 1:
		continue
	prev = dels[0]
	for x in dels[1:]:
		if x - prev != 2:
			break
	else:
		print(i, max(dels))