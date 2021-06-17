def f(x):
	a = 0
	b = 10
	while x > 0:
		c = x % 10
		a += c
		if c < b:
			b = c
		x //= 10
	return a, b


# программа выведет все такие х, взять нужно последнее
for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 15 and res[1] == 5:
		print(x)