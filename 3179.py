def check(a):
	for x in range(1, 1<<15):
		res = (108 % a == 0) and ((x % a == 0) or ((x % 42 != 0) or (x % 68 != 0)))
		if not res:
			return False
	return True
# программа выведет все такие a, найти наибольшее нужно самим

for a in range(1, 1<<15):
	if check(a):
		print(a)