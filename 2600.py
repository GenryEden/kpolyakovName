def countDels(x):
	ans = 0
	for i in range(2, x):
		if x % i == 0:
			if isSimple(x//i) and x//i != i:
				return True
			else:
				return False
	return False

def isSimple(x):
	s = x**0.5
	if x <= 2:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, int(s)+2, 2):
		if x % i == 0:
			return False
	return True
# a = [x for x in range(268312, 336492) if countDels(x) == 2]
a = []
for x in range(268312, 336492+1):
	if countDels(x):
		a.append(x)

print(len(a), min(a))