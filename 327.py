from string import ascii_uppercase
alphabet = '0123456789' + ascii_uppercase
def toCountSystem(x, y):
	ans = ''
	while x:
		ans += alphabet[x%y]
		x //= y
	return ans[::-1]

ans = 0
for y in range(2, len(alphabet)):
	res = toCountSystem(381, y)
	if len(res) == 3 and res[-1] == '3':
		ans = y

print(ans)