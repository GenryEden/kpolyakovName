def f(x):
	l = 0
	m = 0
	while x > 0:
		l += 1
		if m < x % 10:
			m = x % 10
		x //= 10
	return l, m

ans = 0
for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 3 and res[1] == 7:
		ans = x

print(ans)