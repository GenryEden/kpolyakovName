def f(n):
	a = -1
	while n > 9 and a != n % 10:
		a = n % 10
		n //= 10
	return n % 10

for x in range(1000, 9999+1):
	if f(x) == 4:
		break

print(x)