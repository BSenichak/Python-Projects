"""
Задача 2: Виведення чисел у діапазоні
Запросити користувача ввести початкове та кінцеве число.
Вивести всі числа у цьому діапазоні.
"""

s_num = int(input("Перше число"))
e_num = int(input("Друге число"))

for i in range(s_num, e_num + 1):
    print(i, end="😊")