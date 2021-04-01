def f(x):
	a = 0
	b = 0
	while x > 0:
		c = x % 2
		if c == 0:
			a += 1
		else:
			b += 1
		x //= 10
	return a, b

for x in range(1, 1 << 20):
	res = f(x)
	if res[0] == 3 and res[1] == 2:
		break

print(x)