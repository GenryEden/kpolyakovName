def f(d):
	n = 3
	s = 38
	while s <= 1200:
		s += d
		n += 7
	return n

ans = 0
for x in range(1, 1<<20):
	if f(x) == 150:
		ans = x

print(ans)