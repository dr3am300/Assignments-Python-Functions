# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation.

Addition = lambda x, y: x + y
Subtraction = lambda x, y: x - y
Multiplication = lambda x, y: x * y
Division = lambda x, y: x / y

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y

def calculator():
    operation = input("What operation would you like to perform? (Addition, Subtraction, Multiplication, Division): ").capitalize()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if operation == "Addition":
        print(addition(num1, num2))
    elif operation == "Subtraction":
        print(subtraction(num1, num2))
    elif operation == "Multiplication":
        print(multiplication(num1, num2))
    elif operation == "Division":
        print(division(num1, num2))
    else:
        print("Invalid operation. Please try again.")


calculator()

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y

def calculator():
    operation = str(input("What operation would you like to perform? (Addition, Subtraction, Multiplication, Division): ")).capitalize()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if operation == "Addition":
        print(addition(num1, num2))
    elif operation == "Subtraction":
        print(subtraction(num1, num2))
    elif operation == "Multiplication":
        print(multiplication(num1, num2))
    elif operation == "Division":
        if num2 == 0:
            print("Cannot divide by zero. Please try again.")
        else:
            print(division(num1, num2))
    else:
        print("Invalid operation. Please try again.")
calculator()

