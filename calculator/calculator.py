def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operator = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}
def calculator():
    num1 = float(input("number 1>"))
    for symbol in operator:
        print(symbol)
    should_continue = True

    while should_continue:
        operator_Select = input("which operator:")
        selected_operator = operator[operator_Select]
        num2 = float(input("number 2>"))
        answer = selected_operator(num1, num2)

        print(f"{num1} {operator_Select} {num2} = {answer}")

        if input(f"type to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

