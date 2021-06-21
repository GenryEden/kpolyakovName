def check(a):
	for x in range(1, 1<<10):
		for y in range(1, 1<<10):
			res = (2*y + x < a) or (x > 10) or (y > 25)
			if not res:
				return False
	return True

for a in range(1, 1<<20):
	if check(a):
		print(a)
		break