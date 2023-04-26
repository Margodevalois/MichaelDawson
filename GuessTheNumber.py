# Число загадывает компьютер, отгадывает человек
import random

print("\t\tДобро пожаловать в игру 'Угадай число'")
print("Я загадал натуральное число от 1 до 100")
print("Постарайся его угадать!\n")
the_number = random.randint(1, 100)
guess = int(input("Твое предположение: "))
tries = 1
while guess != the_number:
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    guess = int(input("Твое предположение еще раз: "))
    tries += 1
print("Тебе удалось отгадать число! Это действительно", the_number)
print("При этом ты потратил", tries, "попыток\n")

input("\nНажмите Enter, чтобы выйти")