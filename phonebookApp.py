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
        print("-----")
        print(k +":" + v)

phonebook = {}

session = True
while session == True:
    answer = question()
    while answer != 5:
        if answer == 1:
            nameLookup = input("Who would you like to look for? ")
            nameLookupL = nameLookup.lower()
            print("Found entry for {}: {}".format(nameLookup, searchEntry(nameLookupL)))
            break
        elif answer == 2:
            name = input('Name: ')
            number = str(input('Phone Number: '))
            setEntry(name, number)
            print("Entry stored for {}.".format(name))
            break
        elif answer == 3:
            name = input('Who would you like to delete? ')
            nameL = name.lower()
            deleteEntry(nameL)
            print("Entry deleted for {}.".format(name))
            break
        elif answer == 4:
            listEntry()
            break
    if answer == 5:
        session = False
        print("Bye")