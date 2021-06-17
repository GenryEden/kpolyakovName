from functools import cache

@cache
def f(n):
	if n > 20:
		return n*n*n + n
	elif n % 2 == 0:
		return 3*f(n+1) + f(n+3)
	else:
		return f(n+2) + 2*(f(n+3))

def check(x):
	return '1' not in str(x)

cnt = 0
for x in range(1, 1000+1):
	if check(f(x)):
		cnt += 1

print(cnt)