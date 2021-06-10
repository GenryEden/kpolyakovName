from functools import cache

@cache
def f(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	else:
		cnt = f(x-2) + f(x-3)
		if x % 2 == 1:
			cnt += f((x+1)//2)
		return cnt

print(f(11))