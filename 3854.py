def check(x):
	h = hex(x)[2:]
	if h[-1] != 'f':
		return False
	if h[-2] == '1':
		return False
	return x % int('b', 16) == 0

cnt = 0
maximal = 0

for x in range(2827, 18186+1):
	if check(x):
		cnt += 1
		maximal = x

print(cnt, maximal**2)