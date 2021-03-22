from functools import lru_cache

@lru_cache
def f(n):
	if n > 30:
		return n*n + 5*n + 4
	elif n % 2 == 0:
		return f(n+1) + 3*f(n+4)
	else:
		return 2*f(n+2) + f(n+5)

cnt = 0
for x in range(1, 1000+1):
	res = f(x)
	if sum([int(x) for x in str(res)]) == 27:
		cnt += 1
print(cnt)