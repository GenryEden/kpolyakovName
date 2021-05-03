def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

print(toCountSystem(9**8 + 3**5 - 9, 3).count('2'))