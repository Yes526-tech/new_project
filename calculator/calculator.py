# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2
#
# operator = {
# "+": add,
# "-": subtract,
# "*": multiply,
# "/": divide
# }
#
# num1 = int(input("number 1>"))
# for sembol in operator:
#     print(sembol)
# operator_Select = input("which operator:")
# selected_operator = operator[operator_Select]
# num2 = int(input("number 2>"))
# answer = selected_operator(num1, num2)
# print(f"{num1} {operator_Select} {num2} = {answer}")
# operator_Select = input("which operator:")
# selected_operator = operator[operator_Select]
# num3 = int(input("number 3>"))
# second_answer = selected_operator(answer, num3)
# print(f"{answer} {operator_Select} {num3} = {second_answer}")

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(1))

# list1 = [[1, 2, [[[[3]]]]], [["a"], "b"]]
#
#
# def print_items(arr):
#     for item in arr:
#         if type(item) is list:
#             print_items(item) # recursion
#         else:
#             print(item)
#
# print_items(list1)

# 0 1 1 2 3 5 8 13 21 34 55

#
# def generate_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return generate_fibonacci(n - 1) + generate_fibonacci(n - 2)
#
fibo = [0, 1]


def list_fibonacci(n):
    for i in range(1, n):
        fibo.append(fibo[i] + fibo[i - 1])
list_fibonacci(100)

print(fibo)
