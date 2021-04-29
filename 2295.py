a = [x for x in range(1512, 13202+1) if x % 7 == 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 13 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 23 != 0]

print(len(a), max(a))