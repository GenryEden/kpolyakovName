def check(x):
	for i in [2, 8, 16]:
		if x % int('100', i) != 0:
			return False
	for i in [int('110', 2), int('12', 8), int('3a', 16)]:
		if x % i == 0:
			return False
	return True

cnt = 0
minimal = 0

for x in range(10101, 11111):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal)