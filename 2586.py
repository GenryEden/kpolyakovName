def isSimple(x):
	if x <= 2:
		return True
	elif x % 2 == 0:
		return False

	s = (x**0.5) 
	for i in range(3, int(s)+2, 2):
		if x % i == 0:
			return False

	return True

a = [x for x in range(2532000+7, 2532160+1, 10) if isSimple(x)]
for i, x in enumerate(a):
	print(i+1, x)