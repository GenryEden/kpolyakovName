def r(n):
	b = bin(n)[2:]
	return int(b[::-1], 2)

for n in range(1, 500+1):
	if r(n) == 11:
		print(n)