from math import isqrt

def getDels(x, dbg=False):
	dels = []
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			if dbg:
				print(x//i, i)
			dels += [x//i, i]
	if dbg:
		print(dels)
	if isqrt(x)**2 == x:
		dels.remove(isqrt(x))
	return sorted(dels)


for x in range(854321, 1087654+1):
	dels = getDels(x)
	if len(dels) == 0 or len(dels) == 1:
		continue
	prev = dels[0]
	for now in dels[1:]:
		if now - prev != 10:
			break
		prev = now
	else:
		print(x, min(dels))