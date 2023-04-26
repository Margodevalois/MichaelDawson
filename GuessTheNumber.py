# Computer proposes a number, human guess it
import random

print("\t\tWelcome to the game 'Guess the number'")
print("I guessed a natural number from 1 to 100")
print("Try to guess it!\n")
the_number = random.randint(1, 100)
guess = int(input("Your proposal: "))
tries = 1
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Bigger...")
    guess = int(input("Your proposal one more time: "))
    tries += 1
print("You made it! It really was", the_number)
print("You did it with", tries, "tries\n")

input("\nPush Enter, to quit")