# def solution(s):
#     arr = []
#     if (len(s)):
#         seperated = [s[i:i + 2] for i in range(0, len(s), 2)] # ['aa', 'bb', 'c']
#         for item in seperated:
#             if (len(item) == 1):
#                 arr.append(item + '_')
#             else:
#                 arr.append(item)
#         return arr
#     return arr
#
#
#
# print(solution(""))
#
# liste = [i for i in range(0, 11, 2)]
#
# print(liste)


# def addition(n):
#     return n - 5

numbers = [1, 2, 3, 4]
numbers1 = [5, 6, 7, 8, 9]
result = map(lambda n: n * n, numbers,
)
print(list(result))