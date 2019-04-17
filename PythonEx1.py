#1
name = input('What is your name? ')
print("Hello {}".format(name))
print(" ")

#2
name = input('What is your name? ')

letters = 0
while letters < len(name):
    letters += 1

print('HELLO, {}!'.format(name.upper()))
print('YOUR NAME HAS {} LETTERS IN IT! AWESOME!'.format(letters))
print(" ")

#3
print("Please fill in the blanks below: ")
print("____(name)____'s favorite subject in school is ____(subject)____")

name = input('What is name? ')
subject = input('What is subject? ')
madlib_results = "{}'s favorite subject in school is {}.".format(name, subject)

print(madlib_results)
print(" ")

#4
day = int(input('Day (0-6)? ex. Sunday = 0: '))

while(day >= 0 and day <= 6):
    if day == 0:
        print("Sunday")
        break
    elif day == 1:
        print("Monday")
        break
    elif day == 2:
        print("Tuesday")
        break
    elif day == 3:
        print("Wednesday")
        break
    elif day == 4:
        print("Thursday")
        break
    elif day == 5:
        print("Friday")
        break
    elif day == 6:
        print("Saturday")
        break
else:
    print("Not a valid number")
print(" ")

#5
day = int(input('Day (0-6)? ex. Sunday = 0: '))

while(day >= 0 and day <= 6):
    if(day > 0 and day < 6):
        print("Go to work")
        break
    else:
        print("Sleep in")
        break
print(' ')

#6
temp = int(input('Temperature in C? '))
fahrenheit = temp * 1.8 + 32

print('{} F'.format(fahrenheit))
print(' ')

#7
bill_amount = int(input('Total bill amount: '))
service = input('Level of service? Good, fair, or bad?: ')
good = 1.20
fair = 1.15
bad = 1.10

if(service.lower() == 'good'):
    total = good * bill_amount
    print('Total bill amount: {:.2f}'.format(total))
elif (service.lower() == 'fair'):
    total = fair * bill_amount
    print('Total bill amount: {:.2f}'.format(total))
elif(service.lower() == 'bad'):
    total = bad * bill_amount
    print('Total bill amount: {:.2f}'.format(total))
print(' ')

#8
bill_amount = int(input('Total bill amount: '))
service = input('Level of service? Good, fair, or bad?: ')
good = 1.20
fair = 1.15
bad = 1.10

if(service.lower() == 'good'):
    total = good * bill_amount
    print('Total bill amount: {:.2f}'.format(total))
elif (service.lower() == 'fair'):
    total = fair * bill_amount
    print('Total bill amount: {:.2f}'.format(total))
elif(service.lower() == 'bad'):
    total = bad * bill_amount
    print('Total bill amount: {:.2f}'.format(total))

split = int(input('Split how many ways?: '))
new_split = total/split 

print('Amount per person: {:.2f}'.format(new_split))
print(' ')

#9
number = 1
while(number <= 10):
    print(number)
    number += 1

print(' ')

#10
more_coins = input('Would you like a coin? (yes/no): ')
more_coins = more_coins.lower()

coins = 0
while(more_coins == 'yes'):
    coins += 1
    print('You have {} coins.'.format(coins))
    more_coins = input('Would you like another coin? (yes/no): ')

print(' ')
print('You have a wopping total of {} coins'.format(coins))

