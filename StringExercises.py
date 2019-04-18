#1
word = "askjdhlask"
print(word.upper())

#2
word = "alksjdhla"
print(word.capitalize())

#3
word = "kajsdhla"
new = ''
for i in word:
    new = i + new
print(new)

#4
leet = [['A','4'], ['E','3'], ['G','5'], ['I', '1'], ['O', '0'], ['S', '5'], ['T', '7']]
word = 'leet'
word = word.upper()
new_word = ''
for i in word:
    if i in leet:
        new_word = i.replace(leet[i])
    else:
        new_word += i
print(word)