def perebor(alphabet, length):
    if length == 0:
        yield ''
        return
    else:
        for letter in alphabet:
            for word in perebor(alphabet, length-1):
                yield letter+word

def check(word):
    if word[0] == 'Й':
        return False
    if 'ИЙО' in word:
        return False
    return len(set(word)) == len(word)

cnt = 0
last = ''
for word in perebor('НОБЕЛИЙ', 7):
    if check(word):
        last = word
        cnt += 1
print(cnt)
