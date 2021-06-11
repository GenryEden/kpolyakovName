def check(x):
	o = oct(x)[2:]
	if o[-1] != '7' and o[-1] + o[-2] != '66':
		return False
	return x % 12 == 0 or x % 15 != 0

cnt = 0
minimal = 0

for x in range(100, 555555+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal**2)