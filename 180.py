def f(d):
	n = 2
	s = 0
	while s <= 365:
		s += d
		n += 5
	return n

for x in range(1, 1<<20):
	if f(x) == 67:
		break

print(x)