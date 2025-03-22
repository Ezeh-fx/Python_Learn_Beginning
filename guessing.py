import random

secret_key = random.randint(1, 10)
attempts = 3

print("I am thinking of a number between 1 to 10. Can you guess it?")

while attempts > 0:
    try:
        guess = int(input("Take a guess: "))
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess == secret_key:
        print("🎉 Congratulations! You guessed the number correctly.")
        break
    elif guess < secret_key:
        print("Try again. Your guess is too low.")
    else:
        print("Try again. Your guess is too high.")
    
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts left.\n")

if attempts == 0:
    print(f"😢 You have run out of attempts. The correct number was {secret_key}.")

print("Thanks for playing! 🎮")