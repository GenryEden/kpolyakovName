def f(x):
	a = 0
	b = 0
	while x > 0:
		y = x % 10
		if y > 4:
			a += 1
		if y < 6:
			b += 1
		x //= 10
	return a, b

for x in range(10000, 99999+1):
	res = f(x)
	if res[0] == 3 and res[1] == 4:
		break

print(x)