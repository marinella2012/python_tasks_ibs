# Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце
# программы мы вызвали статический метод родительского класса Animal,
# который вывел бы нам количество всех созданных экземпляров.
# Если мы создали трех наследников в предыдущем задании, то наш метод
# должен вывести на экран число 3.
class Animal():
    num_of_ex = 0

    def __init__(self, name):
        self.name = name
        Animal.num_of_ex += 1

    def voice(self):
        return 'Voice!'

    @staticmethod
    def print_num_of_ex():
        return Animal.num_of_ex


class Cat(Animal):
    def voice(self):
        return self.name + ' says: Meow!'


class Dog(Animal):
    def voice(self):
        return self.name + ' says: Woof!'


class Cow(Animal):
    def voice(self):
        return self.name + ' says: Mooo!'


dog = Dog('Dog')
cat = Cat('Cat')
cow = Cow('Cow')

print(Animal.print_num_of_ex())
