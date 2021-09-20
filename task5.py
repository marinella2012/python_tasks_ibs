# Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# Используя модуль random, вывести случайный элемент этого списка.
import random


def num_random(num):
    a = random.choice(num)
    return a


numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(num_random(numbers))
