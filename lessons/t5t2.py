"""
Задача 2: Додавання елементу до словника
Створити пустий словник. Запросити користувача ввести ключ та значення.
Додати ці дані у словник та вивести оновлений словник.
"""
students = {"danylo": 10, "bohdan": 5, "yevgen": 3}
sn = input("Введіть і`мя та клас в форматі 'ім`я-клас'").split("-")
students[sn[0]] = sn[1]
print(students)