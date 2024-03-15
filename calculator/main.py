import os
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    number1 = float(input("What's the first number?:  "))
    while True:
        operation = input(" +, -, *, / \n Pick an operation:  ")
        number2 = float(input("What's the next number?:  "))
        
        function = operations[operation]
        resurt = function(number1, number2)

        print(f"{number1} {operation} {number2} = {resurt}")

        continue_calculator = input(f"type 'y' to continue calculating with {resurt}, or type 'n' to start again")
        
        if continue_calculator == 'y':
            number1 = resurt
            continue
        else:
            os.system("clear")
            break