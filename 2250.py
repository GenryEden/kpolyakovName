def check(A):
	for x in range(1, (64*40)):
		res = not(not(x % 40) or not(x % 64)) or not(x % A)
		if not res:
			return False
	return True


last = 0
for A in range(1, 64*40):
	if check(A):
		last = A

print(last)
