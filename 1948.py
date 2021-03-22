def perebor(alphabet, length):
    if length == 0:
        yield ''
        return
    else:
        for letter in alphabet:
            for word in perebor(alphabet, length-1):
                yield letter+word

def check(word):
    ans = True
    ans &= len(set(word)) == len(word)
    ans &= word[-1] != 'Ь'
    if 'Ь' in word:
        ind = word.index('Ь')
        if 6 != ind != 0:
            ans &= not(word[ind-1] in vowels) or not(word[ind+1] in vowels)
    else:
        return False
    return ans
vowels = 'ЕИ'
print(len([word for word in perebor('ВЕНТИЛЬ', 7) if check(word)]))
