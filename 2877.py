def check(x):
	if x % 7 == 0:
		return False
	if x % 9 == 0:
		return False
	if x % 13 == 0:
		return False
	for s in str(x)[:2]:
		if int(s) % 2 == 0:
			return False
	for s in str(x)[2:]:
		if int(s) % 2 == 1:
			return False
	return True
	
cnt = 0
maximal = 0
minimal = 0
for x in range(57888, 74555+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x
		maximal = x

print(cnt, maximal-minimal)