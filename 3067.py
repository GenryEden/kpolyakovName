from functools import cache

@cache
def f(x):
	if x < 3:
		return 0
	elif x == 3:
		return 1
	else:
		cnt = f(x-1) + f(x-2)
		if x % 2 == 1:
			cnt += f((x+1)//2)
		return cnt

print(f(10))