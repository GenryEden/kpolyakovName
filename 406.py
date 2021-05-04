def f(x):
	l = 0
	m = 1
	while x > 0:
		l += 1
		m *= (x%8)
		x //= 8
	return l, m

ans = 0
for x in range(1, 1<<10):
	res = f(x)
	if res[0] == 3 and res[1] == 120:
		ans = x

print(ans)