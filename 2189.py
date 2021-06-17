def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

print(toCountSystem(25**56 + 5**138 - 5, 5).count('4'))