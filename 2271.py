from functools import lru_cache

@lru_cache
def f(n):
	if n <= 3:
		return n
	elif n % 2 == 0:
		return 2*n + f(n-1)
	else:
		return n*n + f(n-2)

cnt = 0
for x in range(1, 100+1):
	if f(x) % 3 == 0:
		cnt += 1

print(cnt)