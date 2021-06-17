def f(x):
	a = 1
	while x > 0:
		a *= x % 6
		x //= 6
	return a

for x in range(1, 1<<20):
	if f(x) == 40:
		break

print(x)