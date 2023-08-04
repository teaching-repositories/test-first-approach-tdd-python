def add(num1, num2):
    """
    Add two numbers and return the result.

    Args:
        num1 (float): The first number to be added.
        num2 (float): The second number to be added.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Subtract two numbers and return the result.

    Args:
        num1 (float): The number to be subtracted from.
        num2 (float): The number to be subtracted.

    Returns:
        float: The result of subtracting num2 from num1.
    """
    return num1 - num2

def multiply(num1, num2):
    """
    Multiply two numbers and return the result.

    Args:
        num1 (float): The first number to be multiplied.
        num2 (float): The second number to be multiplied.

    Returns:
        float: The product of num1 and num2.
    """
    return num1 * num2

def divide(num1, num2):
    """
    Divide two numbers and return the result.

    Args:
        num1 (float): The dividend.
        num2 (float): The divisor.

    Returns:
        float or str: The result of dividing num1 by num2.
                     If num2 is 0, returns 'Error: Division by zero'.
    """
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error: Division by zero'

def display_menu():
    """
    Display the menu of available operations.
    """
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')

def take_input():
    """
    Take user input for the desired operation.

    Returns:
        str: The user's choice of operation.
    """
    choice = input("Choose an operation: ")
    return choice

def take_numbers_input():
    """
    Take user input for two numbers.

    Returns:
        tuple: A tuple containing the two numbers as floats.
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def call_function(choice):
    """
    Call the appropriate operation function based on the user's choice.

    Args:
        choice (str): The user's choice of operation.

    Prints:
        The result of the operation or 'Invalid input'.
    """
    if choice in functions:
        num1, num2 = take_numbers_input()
        result = functions[choice](num1, num2)
        print("Result: ", result)
    else:
        print("Invalid input")

functions = {'1': add, '2': subtract, '3': multiply, '4': divide}

def main():
    """
    Main function to run the calculator loop.
    """
    while True:
        display_menu()
        choice = take_input()
        
        if choice.lower() == 'q':
            break
        else:
            call_function(choice)

if __name__ == "__main__":
    main()
