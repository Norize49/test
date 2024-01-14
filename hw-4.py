# Задание 1

# string = input("Введіть рядок: ")
#
# letters = 0
# digits = 0
#
# chars = list(string)
#
# for char in chars:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1
#
# print("Кількість літер:", letters)
# print("Кількість цифр:", digits)

# Задание 2

# string = input("Введіть рядок: ")
# symbol = input("Введіть символ для пошуку: ")
#
# count = 0
#
# chars = list(string)
#
# for char in chars:
#     if char == symbol:
#         count += 1
#
# print("Кількість вхождень символу:", count)

# Задание 3

# string = input("Введіть рядок: ")
# search_word = input("Введіть слово для пошуку: ")
# replace_word = input("Введіть слово для заміни: ")
#
# index = string.find(search_word)
#
# if index != -1:
#     string = string[:index] + replace_word + string[index + len(search_word):]
#
# print("Отриманий рядок:", string)

# Задание 4

# string = input("Введіть рядок: ")
#
# print(string[2])
#
# print(string[-2])
#
# print(string[:5])
#
# print(string[:-2])
#
# print(string[::2])
#
# print(string[1::2])
#
# print(string[::-1])
#
# print(string[-1::-2])
#
# print(len(string))