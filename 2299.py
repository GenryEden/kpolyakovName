a = [x for x in range(1107, 9504+1) if x % 9 == 0]
a = [x for x in a if x % 7 != 0]	
a = [x for x in a if x % 15 != 0]	
a = [x for x in a if x % 17 != 0]	
a = [x for x in a if x % 19 != 0]	
print(len(a), min(a))