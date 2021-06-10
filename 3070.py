from functools import cache

@cache
def f(x):
	if x < 4:
		return 0
	elif x == 4:
		return 1
	else:
		cnt = f(x-1)
		if x % 2 == 0 and not(x//2 < 10 < x):
			cnt += f(x//2)
		if not(x-3 < 10 < x):
			cnt += f(x-3)
		return cnt
print(f(20))