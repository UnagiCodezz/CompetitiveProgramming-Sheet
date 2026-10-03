#capitalise the input word, that is, make the first letter capital
word = input()
word = [x for x in word]
if word[0].islower():
    word[0] = word[0].upper()
else:
    pass
for i in word:
    print(i, end="")