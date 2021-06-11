from functools import cache

@cache
def f(n):
	if n == 0:
		return 0
	elif n % 2 == 0:
		return f(n/2)
	else:
		return f(n-1) + 3

cnt = 0
for x in range(1, 1000+1):
	if f(x) == 18:
		cnt += 1
print(cnt)