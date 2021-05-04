def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

print(toCountSystem(4**2016 + 2**2018 - 8**600 + 6, 2).count('1'))