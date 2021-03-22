def check(A):
	for x in range(1, 28*42):
		res = bool(x % A) or (bool(x % 28) or not(x % 42))
		if not res:
			return False
	return True

for A in range(1, 28*42):
	if check(A):
		break

print(A)