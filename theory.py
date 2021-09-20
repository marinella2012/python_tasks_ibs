

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

num = numbers[:]
num = list(numbers)
# print(num)


# уникальная итерация:
#for x in set(num):
#    print(x)
# итерация в обратном порядке:
#for x in reversed(num):
#    print(x)
# исключающая итерация — например, вывести элементы 1-го списка,
# которых нет во 2-м списке:
num2 = list(filter(lambda x: x % 2 != 0 and x > 50, numbers))
for i in set(num).difference(num2):
    print(i)
# С помощью конструктора решим конкретную задачу — отсортируем слова
# в предложении в порядке их длительности:
words = 'jwswsh wu t tttt shjds dsb chd'.split()

wordlens = [(len(word), word) for word in words]

wordlens.sort()

print(' '.join(w for (_, w) in wordlens))

d = dict((x, x**2) for x in range(5))
d = {}.fromkeys(['name', 'age'], 123)
print(d)
