def check(a):
	for x in range(1, 1<<10):
		res = bool(x % a) or (not(x % 14) and not(x % 21))
		if not res:
			return False
	return True

for a in range(1, 1<<20):
	if check(a):
		break

print(a)