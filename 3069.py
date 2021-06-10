from functools import cache

@cache
def f(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	else:
		cnt = f(x-1)
		if x % 2 == 0 and not(x//2 < 7 < x):
			cnt += f(x//2)
		if x % 3 == 0 and not(x//3 < 7 < x):
			cnt += f(x//3)
		return cnt
print(f(28))