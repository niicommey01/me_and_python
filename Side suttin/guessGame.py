import random

def main():
    special_number = random.randint(0, 10)
    guess_count = 0
    guess_limit = 3

    print("Guess a number between 1 and 10")
    while guess_count < guess_limit:
        guess = int(input("Guess a number: "))
        guess_count += 1
        if guess == special_number:
            print("You have won")
            break
    else:
        print(f"With all these chances you still managed to lose. The correct number is {special_number}")




    redo()


def redo():
    again = input("Would you like to lose again?[y/n] ")
    if again == "y":
        main()
    else:
        print("It was good while it lasted. Adios!")

welcome = input("Hello mate! My name is G. What's yours? ")
response = input (f"Hello {welcome}, Would you like to play a guessing game with me?[y/n] ")
if response == "y":
    main()
else:
    print("I hope some other time then")