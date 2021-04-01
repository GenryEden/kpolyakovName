def check(A):
	for x in range(1, 1000):
		for y in range(1, 1000):
			res = (7*y + x < A) or (2*x + 3*y > 98)
			if not res:
				return False

	return True

for A in range(-1000, 1000):
	if check(A):
		break

print(A)