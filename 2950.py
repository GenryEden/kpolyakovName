def f(x):
	a = 0
	b = 1
	while x > 0:
		if x % 2 > 0:
			a += x % 11
		else:
			b *= x % 11
		x //= 11
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 2 and res[1] == 9:
		break
print(x)