def f(d):
	n = 5
	s = 83
	while s <= 1200:
		s += d
		n += 6
	return n

ans = 0
for x in range(1, 1<<20):
	if f(x) == 89:
		ans = x

print(ans)