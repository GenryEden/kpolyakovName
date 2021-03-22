def f(s):
	n = 80
	while s + n < 160:
		s += 15
		n -= 10
	return s

for x in range(1, 1<<20):
	res = f(x)
	if res <= 100:
		break

print(x)