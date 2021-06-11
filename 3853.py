def check(x):
	h = hex(x)[2:]
	if h[-1] != 'a':
		return False
	if h[-2] == '0':
		return False
	return x % int('d', 16) == 0

cnt = 0
minimal = 0

for x in range(1717, 212121+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal**2)