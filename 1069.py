def check(a):
	for x in range(1, 1<<10):
		for y in range(1, 1<<10):
			res = (y + 5*x != 80) or (3*x > a) or (y > a)
			if not res:
				return False
	return True

# программа выведет все такие a, ответ - последнее

for a in range(1, 1<<10):
	if check(a):
		print(a)