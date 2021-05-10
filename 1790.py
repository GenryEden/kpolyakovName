def f(s):
	n = 1
	while s < 51:
		s += 5
		n *= 2
	return n

for x in range(1, 1<<20):
	if f(x) == 64:
		break

print(x)