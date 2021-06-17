def f(s):
	n = 100
	while s - n >= 100:
		s += 20
		n += 40
	return s

for s in range(1, 1<<20):
	if f(s) != s:
		break

print(s)