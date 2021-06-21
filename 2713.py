count = {}

n = int(input())

for _ in range(n):
	a = int(input())
	try:
		count[a] += 1
	except KeyError:
		count[a] = 1

cnt = 0
toAdd = 0

for x in count:
	if str(x) != str(x)[::-1]:
		cnt += (min(count[x], count[int(str(x)[::-1])])//2)*x
		cnt += (min(count[x], count[int(str(x)[::-1])])//2)*int(str(x)[::-1])
	elif count[x] % 2 == 0:
		cnt += count[x]*x
	else:
		cnt += (count[x] - 1)*x
		toAdd = max(toAdd, x)

print(cnt + toAdd)