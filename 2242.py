def check(a):
	for x in range(1, 1<<10):
		res = not(bool(x % a) and bool(x % 6)) or bool(x % 3)
		if not res:
			return False
	return True
# программа выведет все подходящие а, вам нужно взять последний
for a in range(1, 1<<10):
	if check(a):
		print(a)