def isSimple(x):
	if x <= 2:
		return True
	if x % 2 == 0:
		return False
	s = x**0.5
	for i in range(3, int(s) + 2, 2):
		if x % i == 0:
			return False
	return True
cnt = 0
for x in range(4202865, 4202923+1):
	if isSimple(x):
		cnt += 1
		print(cnt, x)