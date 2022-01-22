from lib2to3.pgen2.token import NUMBER
import random

def compare_number_guess(number_attempts):
    while number_attempts!= 0:
        if input("Make a guess: ")== number:
            print("You guessed the right number.")
            return ("You win.")
        else: 
            print("This is not the right number.")
        number_attempts= number_attempts-1
        print(f"You have {number_attempts} attempts remaining to guess the number.")

    return print("You have no more attempts left. You lose.")


def game():
    print("Welcome to the Guessing Game./n I am thinking of a number between 1 and 100.")
    global number
    number = random.randint(1, 100)
    print(f"pssst, the number is {number}.")
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        number_attempts =10
    else: 
        number_attempts =5

    compare_number_guess(number_attempts)


game()