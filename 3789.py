def f(x):
	k = x % 7
	a = 0
	b = 0
	while x > 0:
		d = x % 7
		if d == k:
			a += 1
		b += d
		x //= 7
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 4 and res[1] == 11:
		break

print(x)