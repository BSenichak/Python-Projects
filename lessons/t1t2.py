"""
Задача 2: Конвертація температур Запросити користувача ввести
температуру в градусах Цельсія.
Перетворити цю температуру в градуси Фаренгейта та вивести результат.
"""

t = float(input("input temperature celsium: "))
print(f"{t}C = {(t * (9/5)) + 32}F")