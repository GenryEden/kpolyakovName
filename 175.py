def f(d):
	n = 8
	s = 78
	while s <= 1200:
		s += d
		n += 2
	return n

ans = 0
for x in range(1, 1<<20):
	if f(x) == 46:
		ans = x

print(ans)