def check(x):
	h = hex(x)
	if h[-1] != 'a' and h[-2] + h[-1] != 'ff':
		return False
	return x % 6 == 0

cnt = 0
minimal = 0

for x in range(100, 555555+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal**2)