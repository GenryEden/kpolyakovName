n = int(input())
l = [int(input()) for _ in range(5)]
minimalL = float('inf')
ans = float('inf')
for i in range(n-5):
	minimalL = min(minimalL, l[i%5])
	new = int(input())
	ans = min(ans, new**2 + minimalL**2)
	l[i%5] = new
print(ans)
