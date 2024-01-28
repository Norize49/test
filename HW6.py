# Задание 1

# def product_of_elements(numbers):
#     """
#     Обчислює добуток елементів списку цілих.
#
#     Args:
#         numbers: Список цілих чисел.
#
#     Returns:
#         Добуток елементів списку.
#     """
#
#     product = 1
#     for number in numbers:
#         product *= number
#     return product

# Задание 2

# def find_minimum(numbers):
#     """
#     Знаходить мінімум у списку цілих.
#
#     Args:
#         numbers: Список цілих чисел.
#
#     Returns:
#         Мінімум у списку.
#     """
#
#     minimum = numbers[0]
#     for number in numbers:
#         if number < minimum:
#             minimum = number
#     return minimum

# Задание 3

# def count_primes(numbers):
#     """
#     Визначає кількість простих чисел у списку цілих.
#
#     Args:
#         numbers: Список цілих чисел.
#
#     Returns:
#         Кількість простих чисел у списку.
#     """
#
#     primes = 0
#     for number in numbers:
#         if is_prime(number):
#             primes += 1
#     return primes
#
#
# def is_prime(number):
#     """
#     Визначає, чи є число простим.
#
#     Args:
#         number: Число.
#
#     Returns:
#         True, якщо число просте, False в іншому випадку.
#     """
#
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# Задание 4

# def remove_number(numbers, number):
#     """
#     Видаляє зі списку ціле задане число.
#
#     Args:
#         numbers: Список цілих чисел.
#         number: Число, яке потрібно видалити.
#
#     Returns:
#         Кількість видалених елементів.
#     """
#
#     removed_numbers = 0
#     for i in range(len(numbers)):
#         if numbers[i] == number:
#             del numbers[i]
#             removed_numbers += 1
#     return removed_numbers

# Задание 5

# def merge_lists(list1, list2):
#     """
#     Об'єднує два списки.
#
#     Args:
#         list1: Перший список.
#         list2: Другий список.
#
#     Returns:
#         Об'єднаний список.
#     """
#
#     merged_list = []
#     for number in list1:
#         merged_list.append(number)
#     for number in list2:
#         if number not in merged_list:
#             merged_list.append(number)
#     return merged_list


# Задание 6

# def power_of_elements(numbers, power):
#     """
#     Обчислює ступінь кожного елемента списку цілих.
#
#     Args:
#         numbers: Список цілих чисел.
#         power: Значення для ступеня.
#
#     Returns:
#         Новий список, який містить отримані результати.
#     """
#
#     new_numbers = []
#     for number in numbers:
#         new_number = number ** power
#         new_numbers.append(new_number)
#     return new_numbers
