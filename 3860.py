def toCountSystem(x, y):
	ans = ''
	while x:
		ans += hex(x % y)[2:]
		x //= y
	return ans[::-1]

def sumOfNumerals(x):
	return sum([int(s) for s in str(x)])

for x in range(1, 1<<20):
	res = toCountSystem(125**7 - 25**4 + x, 5)
	if res.count('4') == 15 and res.count('3') == 1 and res.count('1') == 2:
		break

print(x)