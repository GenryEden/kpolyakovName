def check(x):
	return not(x > 41) and not(x % 6)

last = 0
for x in range(-1000, 1000):
	if check(x):
		last = x
print(last)