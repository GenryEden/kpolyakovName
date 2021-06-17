def f(x):
	k = x % 6
	a = 0
	b = 0
	while x > 0:
		d = x % 6
		if d == k:
			a += 1
		b += d
		x //= 6
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 2 and res[1] == 15:
		break

print(x)