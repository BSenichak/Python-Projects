import turtle


def draw_shape(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(angle)


def main():
    turtle.speed(1)
    turtle.bgcolor("white")
    turtle.color("black")

    while True:
        try:
            sides = int(input("Введіть кількість боків (більше 2): "))
            if sides <= 2:
                print("Кількість боків повинна бути більше 2.")
                continue
            break
        except ValueError:
            print("Неправильний формат вводу. Будь ласка, введіть ціле число.")

    while True:
        try:
            size = int(input("Введіть розмір фігури: "))
            break
        except ValueError:
            print("Неправильний формат вводу. Будь ласка, введіть ціле число.")

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    draw_shape(sides, size)

    turtle.done()


if __name__ == "__main__":
    main()
