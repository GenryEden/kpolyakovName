def r(n):
	b = bin(n)[2:]
	if b.count('1') > b.count('0'):
		b += '1'
	else:
		b += '0'
	return int(b, 2)
ans = set()
for i in range(1, 1<<10):
	res = r(i)
	if res < 100:
		ans.add(res)
print(max(ans))