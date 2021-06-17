def check(a):
	for x in range(1, 1<<20):
		res = not(bool(x % a) and not(x % 6)) or bool(x % 3)
		if not res:
			return False
	return True
# программа выведет все такие а, ответ - последнее
for a in range(1, 1<<20):
	if check(a):
		print(a)
