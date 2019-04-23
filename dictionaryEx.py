#1
# phonebook_dict = {
#     'Alice': '222-222-2222',
#     'Bob': '333-333-3333',
#     'Elizabeth': '444-444-4444'
# }

# print(phonebook_dict['Alice'])
# phonebook_dict["Michael"] = "281-330-8004"
# print(phonebook_dict)
# del phonebook_dict['Alice']
# print(phonebook_dict)
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

#2
# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#         {
#             'name': 'Jasmine',
#             'email': 'jasmine@yahoo.com',
#             'interests': ['photography', 'tennis']
#         },
#         {
#             'name': 'Jan',
#             'email': 'jan@hotmail.com',
#             'interests': ['movies', 'tv']
#         }
#     ]
# }

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])


#letterSummary
# letterCount = {}
# def letter_histogram(word):
#     for i in word:
#         if i in letterCount:
#             letterCount["{}".format(i)] += 1
#         else:
#             letterCount["{}".format(i)] = 1
#     print(letterCount)

# letter_histogram('banana')

#Word Summary + ranking
def wordCheck(paragraph):
    wordCount = {}
    wordSeparater = paragraph.lower().replace('.', ' ').replace(',', ' ').split()
    ranking = []
    for word in wordSeparater:
        if word in wordCount:
            wordCount["{}".format(word)] += 1
        else:
            wordCount["{}".format(word)] = 1
    print(wordCount)
    return(wordCount)

def ranking(list):
    rankedList = list
    newList = {}
    for k, v in rankedList.items():
        if v == max(rankedList.values()):
            print(k)
            newList[k] = [v]
            del rankedList[k]
        else:
            print(k)
    print(newList)


sentence = wordCheck("first first first first third third, second second second. fourth")
print(sentence)
ranking(sentence)

