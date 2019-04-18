import random

my_random_number = random.randint(1,10)
answer = int(input("I am thinking of a number between 1 and 10.\n what's the number?" ))

guesses = 4
while answer != my_random_number and guesses > 0:
    if answer >= my_random_number:
        answer = int(input("{} is too high. You have {} guesses left. What's the number? ".format(answer, guesses)))
        guesses -= 1
    elif answer < my_random_number:
        answer = int(input("{} is too low. You have {} guesses left. What's the number? ".format(answer, guesses)))
        guesses -= 1
    elif answer == my_random_number:
        print("Yes! You win!")
else:
    print("You ran out of guesses. You lose!")
