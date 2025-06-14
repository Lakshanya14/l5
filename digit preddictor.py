import random

print("🎉😊Welcome to the Number Guessing game")
print("I am thinking of a number between 1 and 20")
print("you have 5 chances to guess it")

secret_number = random.randint(1, 20)

chances = 5

for guess_count in range(1, chances + 1):
    guess = int(input(f"\nGuess {guess_count}: "))

    if guess == secret_number:
        print("🎉🎉🎉Congratulations! You guessed the number correctly!")
        break
    elif guess < secret_number:
        print("too low try a higher number")
    else:
        print("too high try a lower number")

if guess != secret_number:
    print("\nSorry you have used all of your chances")
    print("the correct number was", secret_number)

print("\nThanks for playing! 😊")    