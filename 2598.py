def check(x):
	prev = 0
	for i in str(x):
		i = int(i)
		if i < prev:
			return False
		prev = i
	return True

ans = 0
for x in range(1395, 22718):
	if check(x):
		ans += x
print(ans)