a = [x for x in range(2055, 9414+1) if x % 4 != 0]
a = [x for x in a if x % 5 != 0]
a = [x for x in a if x % 41 != 0]

a = [x for x in a if (x % 10) + ((x//10)%10) != 5]
mlt = 1
for x in a:
	mlt *= x
print(min(a), str(mlt)[-3:])