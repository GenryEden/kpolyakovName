for x in range(1, 1<<20):
	res = bin(4**1014 - 2**x + 12)[2:]
	if res.count('0') == 2000:
		break

print(x)