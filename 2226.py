def toCountSystem(x, y):
	ans = ''
	while x:
		ans += str(x % y)
		x //=y
	return ans[::-1]

print(toCountSystem(9**9 + 3**21 - 7, 3).count('0'))