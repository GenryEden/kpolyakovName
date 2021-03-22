def toCountSystem(x, y):
	ans = ''
	while x:
		ans += str(x % y)
		x //= y
	return ans[::-1]

print(toCountSystem(36**17 + 6**48 - 17, 6).count('0'))