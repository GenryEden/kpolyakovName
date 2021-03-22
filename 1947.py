def perebor(alphabet, length):
    if length == 0:
        yield ''
        return
    else:
        for letter in alphabet:
            for word in perebor(alphabet, length-1):
                yield letter + word

def check(word):
    if 'Й' in word:
        ind = word.index('Й')
    else:
        return False
    if ind == 0:
        return False
    if ind != 6 and not word[ind+1] in vowels:
        return len(set(word)) == len(word)
    elif ind == 6:
        return len(set(word)) == len(word)
    else:
        return False

vowels = 'АЕ'
print(len([word for word in perebor('АЙСБЕРГ', 7) if check(word)]))
