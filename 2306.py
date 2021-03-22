a = [x for x in range(2478, 7849+1, 2)]
a = [x for x in a if x % 5 != 0]
a = [x for x in a if x % 8 != 0]
a = [x for x in a if x % 9 != 0]
a = [x for x in a if x % 13 != 0]
print(len(a), min(a))