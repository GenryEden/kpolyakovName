def check(a):
	for x in range(1, 1<<10):
		for y in range(1, 1<<10):
			res = (x*y < 4*a) or (x >= 21) or (x < 4*y)
			if not res:
				return False
	return True

for a in range(1, 1<<20):
	if check(a):
		break

print(a)