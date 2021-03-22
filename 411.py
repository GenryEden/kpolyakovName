def f(x):
	a = 0
	b = 0
	while x > 0:
		y = x % 10
		if y > 3:
			a += 1
		if y < 8:
			b += 1
		x //= 10
	return a, b

for x in range(10000, 1<<20):
	res = f(x)
	if res[0] == 4 and res[1] == 2:
		break

print(x)