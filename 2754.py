a = [x for x in range(1325, 15367+1) if x % 13 == 0]
a = [x for x in a if x % 7 != 0]
a = [x for x in a if x % 17 != 0]
a = [x for x in a if x % 19 != 0]
a = [x for x in a if x % 23 != 0]
print(len(a), min(a))