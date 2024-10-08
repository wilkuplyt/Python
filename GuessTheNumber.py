import random

def guess_number():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != number:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")

guess_number()
