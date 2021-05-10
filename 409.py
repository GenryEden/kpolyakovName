def f(x):
	a = 0
	b = 1
	while x > 0:
		a += 1
		b *= x % 10
		x //= 10
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 3 and res[1] == 15:
		break

print(x)