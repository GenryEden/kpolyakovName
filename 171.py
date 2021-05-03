def f(d):
	n = 0
	s = 0
	while s <= 365:
		s += d
		n += 5
	return n

ans = 0
for x in range(1, 1<<20):
	if f(x) == 55:
		ans = x

print(ans)