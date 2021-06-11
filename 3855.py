for x in range(1, 1<<20):
	res = bin(4**2015 + 2**x - 2**2015 + 15)[2:]
	if res.count('1') == 500:
		break

print(x)