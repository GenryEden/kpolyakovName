def check(a):
	for x in range(1, 1<<10):
		for y in range(1, 1<<10):
			res = (5*y + 7*x != 129) or (3*x > a) or (4*y > a)
			if not res:
				return False
	return True

for a in range(1, 1<<20):
	if check(a):
		print(a)