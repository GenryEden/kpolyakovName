def perebor(alphabet, length):
    if length == 0:
        yield ''
        return
    else:
        for letter in alphabet:
            for word in perebor(alphabet, length-1):
                yield letter+word


def check(word):
    return len(set(word)) == 3 and word.count('А') == 2 and not('АА' in word)


cnt = 0
for word in set(perebor('АБАК', 4)):
    if check(word):
        # print(word)21
        cnt += 1
print(cnt)
