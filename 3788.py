def f(x):
	k = x % 5
	a = 0
	b = 0
	while x > 0:
		d = x % 5
		if d == k:
			a += 1
		b += d
		x //= 5
	return a, b

for x in range(1, 1<<20):
	res = f(x)
	if res[0] == 3 and res[1] == 10:
		break

print(x)