s = input()

n = ''
ans = 0

for i in s:
	if i in '0123456789':
		n += i
	else:
		if n:
			if int(n) % 2 == 0:
				ans = max(ans, int(n))
		n = ''

if n:
	if int(n) % 2 == 0:
		ans = max(ans, int(n))

print(ans)