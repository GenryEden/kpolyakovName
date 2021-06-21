def check(a):
	for x in range(1, 1<<10):
		for y in range(1, 1<<10):
			res = (y + 3*x != 60) or (2*x > a) or (y > a)
			if not res:
				return False
	return True

for a in range(1, 1<<20):
	if check(a):
		print(a)