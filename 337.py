from string import ascii_uppercase
alphabet = '0123456789' + ascii_uppercase

def toCountSystem(x, y):
	ans = ''
	while x:
		ans += alphabet[x%y]
		x //= y
	return ans[::-1]

for n in range(2, len(alphabet)):
	res = toCountSystem(87, n)
	if res[-1] == '2' and len(res) >= 3:
		break

print(n)