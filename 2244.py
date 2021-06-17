def check(a):
	for x in range(1, 1<<20):
		res = not(not(x % a) and bool(x % 15)) or (not(x % 18) or not(x % 15))
		if not res:
			return False
	return True

for a in range(1, 1<<20):
	if check(a):
		break

print(a)