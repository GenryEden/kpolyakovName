def check(A):
	for x in range(1, 99*44):
		res = not(x % A) and (A < 10) or bool(x % 44) and bool(x % 99) and (A < 10)
		if not res:
			return False
	return True

for A in range(99*44*9*4, 0, -1):
	if check(A):
		break

print(A)