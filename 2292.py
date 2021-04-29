a = [x for x in range(1012, 9638+1) if x % 3 == 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 13 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]

print(len(a), max(a))