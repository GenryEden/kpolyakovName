def toCountSystem(x, y):
	ans = ''
	while x:
		ans += str(x % y)
		x //= y
	return ans[::-1]

print(toCountSystem(9**14 + 3**18 - 9**5 - 27, 3).count('2'))