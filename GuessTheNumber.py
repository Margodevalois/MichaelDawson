# # Computer proposes a number, human guesses it, 5 tries
# import random
#
# print("\t\tWelcome to the game 'Guess the number'")
# print("I guessed a natural number from 1 to 100")
# print("Try to guess it! But you have only 5 tries\n")
# the_number = random.randint(1, 100)
# guess = int(input("Your proposal: "))
# tries = 1
# while tries < 5:
#     if guess > the_number:
#         print("Lower...")
#         guess = int(input("Your proposal one more time: "))
#         tries += 1
#     elif guess < the_number:
#         print("Bigger...")
#         guess = int(input("Your proposal one more time: "))
#         tries += 1
#     elif guess == the_number:
#         print("\nYou made it! It really was", the_number)
#         break
# else:
#     print("\nYou died!! My number was", the_number)
#
# input("\nPush Enter, to quit")

# Human proposes a number, computer guesses it
import random
import time

print("\t\tWelcome to the game 'Guess the number'\n")
print("\t\tI'll try to guess your number")
print("\t\tLet's start! Think for any number in range from 1 to 100\n")
# system chooses random number and outputs it in 3 sec
a = 1
b = 100
guess = random.randint(a, b)
time.sleep(3)
print("Your number is bigger(B), less(L) or equal(E) to", guess, "?")

answer = ''
tries = 1
while answer != "E":
    answer = input("Bigger, less or equal: ").upper()
    if answer == "B":
        a = guess
        # checkup for a range
        # print('choose from', a, b)
        guess = random.randint(a+1, b)
        print(guess, 'may be this one?')
        tries += 1
    elif answer == "L":
        b = guess
        # checkup for a range
        # print('choose from', a, b)
        guess = random.randint(a, b-1)
        print(guess, 'may be this one?')
        tries += 1
    elif answer != "B" and answer != "L" and answer != "E":
        print('Do not vandalize!')
    else:
        print("I am good! I finished it just with", tries, "tries\n")