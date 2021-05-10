n = int(input())
dp = {}
ans = 0
for _ in range(n):
	a, b = [int(x) for x in input().split()]
	newdp = {}
	for prev in dp:
		prevPos = dp[prev]
		ans = max(ans, prevPos)
		if prev == a:
			if b in newdp:
				newdp[b] = max(newdp[b], prevPos+1)
			else:
				newdp[b] = prevPos + 1
		elif prev == b:
			if a in newdp:
				newdp[a] = max(newdp[a], prevPos+1)
			else:
				newdp[a] = prevPos + 1
	if a not in newdp:
		newdp[a] = 1
	if b not in newdp:
		newdp[b] = 1

	dp = newdp

for prev in dp:
	prevPos = dp[prev]
	ans = max(ans, prevPos)

print(ans)