from string import ascii_uppercase
alphabet = '0123456789' + ascii_uppercase
def toCountSystem(x, y):
	ans = ''
	while x:
		ans += alphabet[x%y]
		x //= y
	return ans[::-1]

for y in range(2, len(alphabet)):
	res = toCountSystem(67, y)
	if len(res) == 4 and res[-1] == '1':
		break

print(y)