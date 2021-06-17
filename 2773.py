def f(n):
	b = bin(n)[2:]
	b = b.zfill(8)
	b = b[:-1]
	b = b[::-1]
	return int(b, 2)

for x in range(99, 0, -1):
	if f(x) == x:
		break

print(x)