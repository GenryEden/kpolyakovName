def check(x):
	if x % 6 == 0:
		return False
	if x % 7 == 0:
		return False
	if x % 8 == 0:
		return False
	for i, s in enumerate(str(x)):
		if (i == 2 or i == 4) and (int(s) % 2 == 1):
			return False
		if (4 != i != 2) and (int(s) % 2 == 0):
			return False
	return True

cnt = 0
maximal = 0
minimal = 0

for i in range(33333, 55555+1):
	if check(i):
		cnt += 1
		if cnt == 1:
			minimal = i
		maximal = i

print(cnt, maximal-minimal)