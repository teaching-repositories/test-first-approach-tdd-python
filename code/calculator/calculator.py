def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 != 0:
    return num1 / num2
  else:
    return 'Error: Division by zero'

def display_menu():
      print('1. Add')
      print('2. Subtract')
      print('3. Multiply')
      print('4. Divide')

def take_input():
    choice = input("Choose an operation: ")
    return choice

def take_numbers_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def call_function(choice):
    if choice in functions:
        num1, num2 = take_numbers_input()
        result = functions[choice](num1, num2)
        print("Result: ", result)
    else:
        print("Invalid input")
  
functions = {'1': add, '2': subtract, '3': multiply, '4': divide}
def main():
    while True:
        display_menu()
        choice = take_input()
        
        if choice.lower() == 'q':
            break
        else:
            call_function(choice)

if __name__ == "__main__":
    main()