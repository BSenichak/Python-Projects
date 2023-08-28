import painter

while True:
    print('Привіт, виберіть фігуру')
    print('1 - square')
    print('2 - circle')
    print('3 - star')
    userChoice = int(input())
    painter.clear()
    if 1 == userChoice:
        painter.draw_square()
    if 2 == userChoice:
        painter.draw_circle()
    if 3 == userChoice:
        painter.draw_star()
