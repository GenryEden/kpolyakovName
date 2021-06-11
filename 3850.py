def sumOfDels(x):
	s = 0
	for i in range(2, x):
		if x % i == 0:
			s += i
	return s

def check(x):
	if x % 5 == 0:
		return False
	return sumOfDels(x) > 40

cnt = 0
maximal = 0
minimal = 0

for x in range(123, 1151+1):
	if check(x):
		cnt += 1
		if cnt == 1:
			minimal = x
		maximal = x

print(cnt, maximal-minimal)