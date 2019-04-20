# #1
# word = "askjdhlask"
# print(word.upper())

# #2
# word = "alksjdhla"
# print(word.capitalize())

# #3
# word = "kajsdhla"
# new = ''
# for i in word:
#     new = i + new
# print(new)

# #4
# leet = {'A':'4', 'E':'3', 'G':'5', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
# word = 'kill me now'
# word = word.upper()
# new_word = ''
# for i in word:
#     if i in leet:
#         i = i.replace(i, leet[i])
#         new_word += i
#     else:
#         new_word += i
# print(new_word)


#5
word = input('Give me a word: ')
word = word.lower()
print(len(word))
for i in range(len(word)):
    if word[i] == word[i+1]:
        print(word[0:i] + word[i]*3 + word[i:len(word)])
    
