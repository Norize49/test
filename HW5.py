# Задание 1

# import random
#
# # Створення списку випадкових чисел
# numbers = [random.randint(-100, 100) for _ in range(10)]
#
# # Сума негативних чисел
# negative_numbers = [x for x in numbers if x < 0]
# sum_of_negative_numbers = sum(negative_numbers)
#
# # Сума парних чисел
# even_numbers = [x for x in numbers if x % 2 == 0]
# sum_of_even_numbers = sum(even_numbers)
#
# # Сума непарних чисел
# odd_numbers = [x for x in numbers if x % 2 == 1]
# sum_of_odd_numbers = sum(odd_numbers)
#
# # Добуток елементів з кратними індексами 3
# multiples_of_3 = [x for x in numbers if x % 3 == 0]
# product_of_multiples_of_3 = 1
# for x in multiples_of_3:
#     product_of_multiples_of_3 *= x
#
# # Добуток елементів між мінімальним та максимальним елементом
# min_number = min(numbers)
# max_number = max(numbers)
# product_of_elements_between_min_and_max = 1
# for x in numbers:
#     if x > min_number and x < max_number:
#         product_of_elements_between_min_and_max *= x
#
# # Сума елементів, що знаходяться між першим та останнім позитивними елементами
# positive_numbers = [x for x in numbers if x > 0]
# if positive_numbers:
#     first_positive_number = positive_numbers[0]
#     last_positive_number = positive_numbers[-1]
#     sum_of_elements_between_first_and_last_positive_numbers = sum(positive_numbers[positive_numbers.index(first_positive_number) + 1:positive_numbers.index(last_positive_number)])
# else:
#     sum_of_elements_between_first_and_last_positive_numbers = 0
#
# # Виведення результатів
# print("Сума негативних чисел:", sum_of_negative_numbers)
# print("Сума парних чисел:", sum_of_even_numbers)
# print("Сума непарних чисел:", sum_of_odd_numbers)
# print("Добуток елементів з кратними індексами 3:", product_of_multiples_of_3)
# print("Добуток елементів між мінімальним та максимальним елементом:", product_of_elements_between_min_and_max)
# print("Сума елементів, що знаходяться між першим та останнім позитивними елементами:", sum_of_elements_between_first_and_last_positive_numbers)

# Задание 2

# import random
#
# # Створення списку випадкових чисел
# numbers = [random.randint(-100, 100) for _ in range(10)]
#
# # Список парних чисел
# even_numbers = [x for x in numbers if x % 2 == 0]
#
# # Список непарних чисел
# odd_numbers = [x for x in numbers if x % 2 == 1]
#
# # Список негативних чисел
# negative_numbers = [x for x in numbers if x < 0]
#
# # Список позитивних чисел
# positive_numbers = [x for x in numbers if x >= 0]
#
# # Виведення результатів
# print("Список парних чисел:", even_numbers)
# print("Список непарних чисел:", odd_numbers)
# print("Список негативних чисел:", negative_numbers)
# print("Список позитивних чисел:", positive_numbers)
