def check(x):
	if sum([int(s) for s in oct(x)[2:]]) % 19 != 0:
		return False
	m = 1
	for s in oct(x)[2:]:
		m *= int(s)
	return m % 5 == 0
cnt = 0
minimal = 0
for x in range(12345, 67890+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x

print(cnt, minimal)