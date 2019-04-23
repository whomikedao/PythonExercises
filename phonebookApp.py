def menu():
    print("""
Electronic Phone Book
=====================
1. Look up an entry 
2. Set an entry 
3. Delete an entry 
4. List all entries  
5. Quit
=====================""")

def question():
    menu()
    answer = int(input("What do you want to do (1-5)? "))
    return answer

def searchEntry(name):
    name = str(name)
    return phonebook.get(name)

def setEntry(inputName, inputPhonenumber):
    name = str(inputName).lower()
    phonenumber = str(inputPhonenumber)
    phonebook[name] = phonenumber

def deleteEntry(name):
    del phonebook[name]

def listEntry():
    for k, v in phonebook.items():
        print(k, v)

phonebook = {}

menu()
question()
session = True
while session == True:
    if question == 1:
        nameLookup = input("Who would you like to look for? ")
        print(searchEntry(nameLookup))
        menu()
        question()
    if question == 2:
        name = input('Name: ')
        number = str(input('Phone Number: '))
        setEntry(name, number)
        menu()
        question()
    if question == 3:
        name = input('Who would you like to delete? ')
        name = name.lower()
        deleteEntry(name)
        menu()
        question()
    if question == 4:
        listEntry()
        menu()
        question()
    if question == 5:
        session = False 











