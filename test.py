number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
number3 = float(input("Введіть третє число: "))

print("Виберіть операцію:")
print("1. Максимальне значення")
print("2. Мінімальне значення")
print("3. Середнє арифметичне")

oper = int(input("Введіть номер операції: "))

if oper == 1:
    print("Максимальне значення:", max(number1, number2, number3))
elif oper == 2:
    print("Мінімальне значення:", min(number1, number2, number3))
elif oper == 3:
    print("Середнє арифметичне:", min(number1, number2, number3))
else:
    print("Невірний номер операції")

