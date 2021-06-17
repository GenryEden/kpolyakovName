n = int(input())
max6 = 0
max3 = 0
max2 = 0
max1 = 0
ans = 0
for i in range(n):
	a = int(input())
	if a % 6 == 0:
		ans = max(ans, a*max6, a*max3, a*max2, a*max1)
		max6 = max(a, max6)	
	elif a % 3 == 0:
		ans = max(ans, a*max6, a*max2)
		max3 = max(a, max3)	
	elif a % 2 == 0:
		ans = max(ans, a*max6, a*max3)
		max2 = max(a, max2)
	else:
		ans = max(ans, a*max6)
		max1 = max(a, max1)

print(ans)