from functools import lru_cache

@lru_cache
def f(n):
	if n <= 3:
		return n
	elif n % 2 == 0:
		return 2*n*n + f(n-1)
	else:
		return n*n*n + n + f(n-1)

cnt = 0
for x in range(1, 1<<10):
	if f(x) < 10**7:
		cnt += 1

print(cnt)