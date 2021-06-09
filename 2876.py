def check(x):
	if x % 9 == 0:
		return False
	if x % 13 == 0:
		return False
	if x % 17 == 0:
		return False
	for s in str(x)[-3:]:
		if int(s) % 2 == 0:
			return False
	for s in str(x)[:-3]:
		if int(s) % 2 == 1:
			return False
	return True

maximal = 0
minimal = 0
cnt = 0
for x in range(64444, 77563+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x
		maximal = x

print(cnt, maximal-minimal)