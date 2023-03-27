from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    math_calculation()

def math_calculation():
    print(logo)

    num1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)

    operator = input("Pick an operation from above: ")

    num2 = float(input("Enter next number: "))

    calculation_function = operations[operator]

    result = calculation_function(num1, num2)

    print(f"{num1} {operator} {num2} = {result:.4f}")

    return result

def continue_calculation(last_result):
    num1 = last_result

    for key in operations:
        print(key)

    operator = input("Pick an operation from above: ")

    num2 = float(input("Enter next number: "))

    result = operations[f"{operator}"](num1, num2)

    print(f"{num1} {operator} {num2} = {result:.4f}")

    return result

user_calculation = math_calculation()

should_continue = False
while should_continue != True:
    user_continue = input(f"if you would like to conitnue calculation with {user_calculation}, enter 'y'. to start new calculation, enter 'n': ").lower()
    if user_continue == 'y':
        user_calculation = continue_calculation(user_calculation)
       
    else:
        # new_calculation = math_calculation
        switch = True
        calculator()