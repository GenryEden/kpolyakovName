def check(A):
	for x in range(1, 15*28):
		for y in range(1, 15*28):
			res = (-y + 2*x < A) or (x > 15) or (y > 28)
			if not res:
				return False
	return True

for A in range(-2**10, 2**10):
	if check(A):
		break

print(A)