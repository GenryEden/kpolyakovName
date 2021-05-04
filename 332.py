def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

print(toCountSystem(4**2014 + 2**2015 - 8, 2).count('1'))