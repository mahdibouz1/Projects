import os

# This file will store the equations
THE_EQUATIONS_FILE_ = "equations.txt"

def performs_calculation():
    """This function performs a calculation and saves it to file equations.txt"""
    try:
        number1 = float(input('Please enter the first number : '))
        operator = input('Please enter an operator (+, -, * or /) : ').strip()
        number2 = float(input('Please enter the second number : '))

        if operator not in ['+', '-', '*', '/']:
            print('Invalid operator given! Instead please use +, -, *, or / ')
            return

        if operator == "/" and number2 == 0:
            print('Error: Dividing by zero is not allowed ')
            return

        # Perform the calculation using inputs from user
        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        elif operator == '/':
            result = number1 / number2

        # Creating an equation string
        equation = f'{number1} {operator} {number2} = {result}'

        # Saving to the file
        with open(THE_EQUATIONS_FILE_, "a") as file:
            file.write(equation + "\n")

        print('The Result is :', result)

    except ValueError:
        print('Invalid input! Please try again input numbers ')

def prints_equations():
    """This functions prints all previous equations from the file"""
    if not os.path.exists(THE_EQUATIONS_FILE_):
        print("No previous equations found.")
        return

    try:
        with open(THE_EQUATIONS_FILE_, "r") as file:
            equations = file.readlines()

        if not equations:
            print('No previous equations found, try again please')
        else:
            print('\nPrevious Equations : ')
            for equation in equations:
                print(equation.strip())

    except Exception as e:
        print(f'Sorry an error occurred while reading the file: {e}')

def main():
    """This is the main loop of the calculator app"""
    while True:
        print("\nWelcome to the Simple Calculator")
        print("1. Perform a calculation")
        print("2. Show previous calculations")
        print("3. Exit")

        decision = input("Enter your choice (1/2/3)").strip()

        if decision == '1':
            performs_calculation()
        elif decision == '2':
            prints_equations()
        elif decision == '3':
            print('Goodbye, have a good day')
            break
        else:
            print('Invalid choice given! Please try again,enter 1, 2, or 3 ')

if __name__ == "__main__":
    main()
