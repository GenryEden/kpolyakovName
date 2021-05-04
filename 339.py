def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

a = toCountSystem(abs(4**812 + 8**800 - 2**3125 - 8**65 - 4**312 + 130), 2)
print(a.count('0'))

# ALERT! Число отрицаетльно, его нужно absить, иначе функция будет выполняться вечно