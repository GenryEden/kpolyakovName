def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x%y)[2:]
		x //= y
	return ans[::-1]

# программа выведет все цифры и их количество, ответ найдете сами
res = toCountSystem(9**5 + 3**7 - 14, 3)
for n in set(res):
	print(n, res.count(n))