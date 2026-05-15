import random

def main():
    
    hidden_number = random.randint(1, 101)

    print("I'm thinking of a number from 1 to 100. Try to guess the number")
    number_of_guesses = 0
    print(hidden_number)

    while True:
        player_guess = int(input("Guess a number: "))
        number_of_guesses += 1

        if hidden_number < player_guess:
            print("lower")
        elif hidden_number > player_guess:
            print("higher")
        elif hidden_number == player_guess:
            print("You WIN!! You got the number in", number_of_guesses, "guesses" if number_of_guesses > 1 else "guess")
            break
        else:
            print("Invalid guess")



if __name__ == "__main__":
    main()