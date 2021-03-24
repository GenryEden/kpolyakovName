def check(A):
	for x in range(1, 30*40):
		for y in range(1, 30*40):
			res = ((y - 40 < A) and (30 - y < A)) or (x*y > 20)
			if not res:
				return False
	return True

for A in range(-100, 100):
	if check(A):
		break

print(A)
