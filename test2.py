meters = float(input("Введіть кількість метрів: "))


print("Виберіть одиницю виміру:")
print("1. Мілі")
print("2. Дюйми")
print("3. Ярди")


unit = int(input("Введіть номер одиниці виміру: "))

if unit == 1:
    miles = meters / 1609.344
    print("Кількість миль:", miles)
elif unit == 2:
    inches = meters * 39.3701
    print("Кількість дюймів:", inches)
elif unit == 3:
    yards = meters / 0.9144
    print("Кількість ярдів:", yards)
else:
    print("Невірний номер одиниці виміру")