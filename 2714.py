def f(s):
	prev = 0
	cnt = 0
	ans = 0
	for l in s:
		l = int(l)
		if l > prev:
			cnt += 1
		else:
			if cnt == 5:
				ans += 1
			cnt = 1
		prev = l
	return ans

s = input()
print(f(s))