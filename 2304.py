a = [x for x in range(1170, 8367+1) if x % 3 == 0 or x % 7 == 0]
a = [x for x in a if x % 11 != 0]
a = [x for x in a if x % 13 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]

print(len(a), min(a))