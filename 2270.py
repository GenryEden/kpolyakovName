from functools import lru_cache

def f(n):
	if n <= 3:
		return n
	elif n % 2 == 0:
		return n + f(n-1)
	else:
		return n*n + f(n-2)
ans = 0
for x in range(1, 1<<20):
	if f(x) < 10**8:
		ans += 1
	else:
		break