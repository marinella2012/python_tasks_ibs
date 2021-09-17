# Вывести на экран сумму четных чисел от 1 до 100 включительно,
# используя функцию range()


def range_func():
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum += i
    return sum


print(range_func())
