buf = [0]*6
minNech = float('inf')
ans = float('inf')

n = int(input())

for x in range(6):
	buf[x] = int(input())

for x in range(n-6):
	res = buf[x%6]
	if res % 2 != 0:
		minNech = min(minNech, res)
	buf[x%6] = int(input())
	if buf[x%6] % 2 != 0:
		ans = min(ans, buf[x%6]*minNech)

print(ans)