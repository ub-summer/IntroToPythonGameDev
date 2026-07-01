import random

secret = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100")
print("Can you guess it?")
print()

winner = False
guesses = 0

while not winner:
    guess = input("Enter you're guess: ")
    guess = int(guess)
    guesses = guesses + 1
    if secret > guess:
        print("higher")
    elif secret < guess:
        print("lower")
    else:
        print("You guessed the number! You win!")
        winner = True

print("You guesses the number in " + str(guesses) + " guesses")
