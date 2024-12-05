
def operations():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            break
        except ValueError:
            print("That looks like a number to you?")

    while True:
        try:
            num2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Ths doesn't look like a number to me")

    while True:
        operation = input("What would you like to do with those numbers?( a for add, s for subtract, m for multiply, d for divide) ").lower()

        if operation == "a":
            added = num1 + num2
            print(added)
            break
        elif operation == "s":
            difference = num1 - num2
            print(difference)
            break
        elif operation == "d":
            divided = num1 / num2
            print(divided)
            break
        elif operation == "m":
            multiplied = num1 * num2
            print(multiplied)
            break
        else:
            print("I don't think that's among the list of operations")

    any_other()


def any_other():
    while True:
        redo = input("Do you have any other operation you would like to do? [y/n]").lower()
        if redo == "y":
            operations()
        else:
            print("Nice being of help. See you soon")
        break


operations()
