def f(s):
	n = 2
	while s < 37:
		s += 3
		n *= 2
	return n

for s in range(1,1<<20):
	if f(s) == 128:
		break

print(s)