from functools import cache

@cache
def f(x):
	if x == 0:
		return 0
	if x % 2 == 0:
		return f(x/2) + 3
	else:
		return 2*f(x-1) + 1

ans = set()

for x in range(1, 1000+1):
	ans.add(f(x))

print(len(ans))