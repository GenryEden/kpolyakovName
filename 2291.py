a = [x for x in range(1033, 7737+1) if x % 5 == 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]
a = [x for x in a if x % 23 != 0]

print(len(a), max(a))