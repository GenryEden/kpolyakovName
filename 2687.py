mods = [float('inf')]*16
ans = 0
n = int(input())
for _ in range(n):
	a, b = [int(x) for x in input().split()]
	ans += max(a, b)
	dist = abs(a - b)
	mods[dist%16] = min(dist, mods[dist%16])


# 11828
# 41262097
if ans % 16 == 10:
	print(ans - min(mods[1:]))
else:
	print(ans)