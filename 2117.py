s = '5'*150

while '5555' in s:
    s = s.replace('5555', '33')
    s = s.replace('333', '5')
    
print(s)