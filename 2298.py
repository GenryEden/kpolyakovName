a = [x for x in range(200, 9120+1) if x % 8 == 0]
a = [x for x in a if x % 7 != 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]

print(len(a), min(a))