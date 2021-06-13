def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(1))

list1 = [[1, 2, [[[[3]]]]], [["a"], "b"]]


def print_items(arr):
    for item in arr:
        if type(item) is list:
            print_items(item) # recursion
        else:
            print(item)

print_items(list1)

0 1 1 2 3 5 8 13 21 34 55


def generate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return generate_fibonacci(n - 1) + generate_fibonacci(n - 2)

fibo = [0, 1]


def list_fibonacci(n):
    for i in range(1, n):
        fibo.append(fibo[i] + fibo[i - 1])
list_fibonacci(100)

print(fibo)
