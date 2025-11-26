from random import randint

name = input("What is your name? ")
secret_number = randint(1, 100)

print(f"Okay, {name}, I've thought of a number between 1 and 100.")
print("You have 8 attempts to guess it.")

for attempt in range(1, 9):
    guess = int(input(f"\nAttempt {attempt}: What is the number? "))

    if guess < 1 or guess > 100:
        print("You have chosen a number that is not allowed.")
    elif guess < secret_number:
        print("Your answer is incorrect. You have chosen a number less than the secret number.")
    elif guess > secret_number:
        print("Your answer is incorrect. You have chosen a number higher than the secret number.")
    else:
        print(f"Congratulations {name}! You have won in {attempt} attempts.")
        break

if guess != secret_number:
    print(f"\nSorry, you have exhausted all 8 attempts. The secret number was {secret_number}.")