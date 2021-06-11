from math import isqrt

def check(x):
	cnt = 0
	if isqrt(x)**2 == x:
		cnt -= (isqrt(x)+1) % 2
	for i in range(2, isqrt(x)+1):
		if x % i == 0:
			if i % 2 == 0:
				cnt += 1
			else:
				return False
			if x//i % 2 == 0:
				cnt += 1
			else:
				return False
		if cnt > 3:
			return False
	return cnt == 3

# for i in range(100000000, 101000000+1):
# 	if check(i):
# 		xp = 0
# 		for x in range(2, i):
# 			if i % x == 0:
# 				if xp == 0:
# 					xp = x
# 				else:
# 					print(i, i//x)
# 					break