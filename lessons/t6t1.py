"""
Задача 1: Перевірити наявність ключа
Створити словник з парами "ім'я": "вік". Запросити користувача ввести ім'я.
Перевірити, чи є це ім'я ключем у словнику,
та вивести вік цієї особи, якщо ключ знайдено, або повідомлення про те, що такого імені немає, якщо ключ не знайдено.
"""

peronal = {"jhon": 55, "antony": 10, "alex": 25}

name = input("Введіть ім'я")
if name in peronal:
    age = peronal[name]
    print(f"Вік особи {name}: {age} років")
else:
    print("такої особи немає в словнику")