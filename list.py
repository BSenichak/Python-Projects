def add_product(products, name, quantity):
    if name in products:
        products[name] += quantity
    else:
        products[name] = quantity

def remove_product(products, name, quantity):
    if name in products:
        if products[name] > quantity:
            products[name] -= quantity
        else:
            del products[name]
    else:
        print("Продукт не знайдено у списку.")

def view_products(products):
    print("Список продуктів:")
    for product, quantity in products.items():
        print(f"{product}: {quantity}")

def main():
    products = {}

    while True:
        print("\nМеню:")
        print("1. Додати продукт")
        print("2. Видалити продукт")
        print("3. Переглянути список продуктів")
        print("4. Вийти")

        choice = input("Виберіть дію (1/2/3/4): ")

        if choice == '1':
            name = input("Введіть назву продукту: ")
            quantity = int(input("Введіть кількість: "))
            add_product(products, name, quantity)
        elif choice == '2':
            name = input("Введіть назву продукту: ")
            quantity = int(input("Введіть кількість: "))
            remove_product(products, name, quantity)
        elif choice == '3':
            view_products(products)
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
