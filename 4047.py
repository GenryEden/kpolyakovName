def r(n):
	if n % 3 == 0:
		n //= 3
	else:
		n -= 1
	if n % 5 == 0:
		n //= 5
	else:
		n -= 1
	if n % 11 == 0:
		n //= 11
	else:
		n -= 1
	return n

cnt = 0
for n in range(1, 1<<20):
	if r(n) == 8:
		cnt += 1
print(cnt)