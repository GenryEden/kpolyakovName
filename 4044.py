def r(n):
	if n % 2 == 0:
		n //= 2
	else:
		n -= 1
	if n % 3 == 0:
		n //= 3
	else:
		n -= 1
	if n % 7 == 0:
		n //= 7
	else:
		n -= 1
	return n 

cnt = 0

for n in range(2, 1<<20):
	if r(n) == 2:
		cnt += 1