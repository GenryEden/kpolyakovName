def check(A):
	for x in range(1, 200*42):
		res = (not(not(x % 36) and not(x % 42)) or not(x % A)) and (A*(A-25) < 25*(A+200))
		if not res:
			return False
	return True

last = -1
for A in range(1, 1<<20):
	if check(A):
		last = A

print(last)