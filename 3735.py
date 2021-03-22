def check(x):
	if x % 2 != 0:
		return False
	if bin(x)[2:].count('1') != 3:
		return False
	return x % 8 == 0 and x % 5 != 0

a = [x for x in range(64, 1025) if check(x)]
print(len(a), max(a))