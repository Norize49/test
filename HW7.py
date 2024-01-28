# Задание 1

# def power(number, power):
#     """
#     Знаходить ступінь числа.
#
#     Args:
#         number: Число.
#         power: Ступінь.
#
#     Returns:
#         Ступінь числа.
#     """
#
#     if power == 0:
#         return 1
#     elif power == 1:
#         return number
#     else:
#         return number * power(number, power - 1)


# Задание 2

# def print_stars(n):
#     """
#     Виводить N зірок у ряд.
#
#     Args:
#         n: Кількість зірок.
#     """
#
#     if n == 0:
#         return
#     else:
#         print("*", end="")
#         print_stars(n - 1)
#
# # Илюстрация:
#
# print_stars(5)

# Задание 3

# def sum_in_range(a, b):
#     """
#     Обчислює суму всіх чисел у діапазоні від a до b.
#
#     Args:
#         a: Початкове число.
#         b: Кінцеве число.
#
#     Returns:
#         Сума всіх чисел у діапазоні.
#     """
#
#     if a > b:
#         return 0
#     else:
#         return a + sum_in_range(a + 1, b)


# Задание 4 (Доп)


# import random
#
# def find_min_sum_sequence_start_position(array):
#     """
#     Знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.
#
#     Args:
#         array: Одновимірний масив із 100 цілих чисел.
#
#     Returns:
#         Позиція початку послідовності.
#     """
#
#     if len(array) < 10:
#         return None
#
#     best_start_position = 0
#     best_sum = sum(array[:10])
#     for i in range(1, len(array) - 9):
#         current_sum = sum(array[i:i + 10])
#         if current_sum < best_sum:
#             best_start_position = i
#             best_sum = current_sum
#
#     return best_start_position
#
#
# array = [random.randint(0, 100) for _ in range(100)]
# print(array)
#
# start_position = find_min_sum_sequence_start_position(array)
#
# print("Позиція початку послідовності:", start_position)
