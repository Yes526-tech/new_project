def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def division(a, b):
    return a / b

first_number= float(input("number:"))
choice = input("+ \n- \n* \n/\nwhich operator:")
if choice == "+":
    second_number = float(input("number:"))
    add_number = add(first_number, second_number)
    choice_add_number = input("another number:'y' or 'n':\n ")
    if choice_add_number == "n":
        print(add_number)
    else:
        another_number = float(input("add number:\n"))
        add(add_number, another_number)
if choice == "-":
    second_number = float(input("number:"))
    subtract_number = subtract(first_number, second_number)
    choice_add_number = input("another number:'y' or 'n':\n ")
    if choice_add_number == "n":
        print(subtract_number)
    else:
        another_number = float(input("add number:\n"))
        subtract(subtract_number, another_number)

if choice == "*":
    second_number = float(input("number:"))
    multiply_number = multiply(first_number, second_number)
    choice_add_number = input("another number:'y' or 'n':\n ")
    if choice_add_number == "n":
        print(multiply_number)
    else:
        another_number = float(input("add number:\n"))
        multiply(multiply_number, another_number)

if choice == "/":
    second_number = float(input("number:"))
    division_number = division(first_number, second_number)
    choice_add_number = input("another number:'y' or 'n':\n ")
    if choice_add_number == "n":
        print(division_number)
    else:
        another_number = float(input("add number:\n"))
        division(division_number, another_number)

