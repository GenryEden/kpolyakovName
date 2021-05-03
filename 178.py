def f(d):
	n = 3
	s = 57
	while s <= 1200:
		s += d
		n += 4
	return n

for x in range(1, 1<<20):
	if f(x) == 63:
		break

print(x)