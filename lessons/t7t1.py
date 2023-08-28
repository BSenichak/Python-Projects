def sqare(width, height):
    s = width * height
    return s

print(sqare(5, 10))

def avarange(numbers):
    return sum(numbers)/len(numbers)

a = avarange([35, 56, 75,1,3,4])
print(a)

def parity(number: 1):
    if number % 2 == 0:
        return True
    else:
        return False

print(parity(2))
print(parity(3))
print(parity(238546873465934))