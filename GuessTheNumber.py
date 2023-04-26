# Computer proposes a number, human guesses it, 5 tries
import random

print("\t\tWelcome to the game 'Guess the number'")
print("I guessed a natural number from 1 to 100")
print("Try to guess it! But you have only 5 tries\n")
the_number = random.randint(1, 100)
guess = int(input("Your proposal: "))
tries = 1
while tries < 5:
    if guess > the_number:
        print("Lower...")
        guess = int(input("Your proposal one more time: "))
        tries += 1
    elif guess < the_number:
        print("Bigger...")
        guess = int(input("Your proposal one more time: "))
        tries += 1
    elif guess == the_number:
        print("\nYou made it! It really was", the_number)
        break
else:
    print("\nYou died!! My number was", the_number)

input("\nPush Enter, to quit")

