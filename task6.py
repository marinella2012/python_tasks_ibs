# Есть класс Animal c одним методом voice().
# class Animal:
# def voice(self):
# pass
# 1. Создать от него три класса наследника и для каждого сделать свою
# реализацию метода voice().
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого
# переопределенный метод voice().
class Animal():
    def __init__(self, name):
        self.name = name

    def voice(self):
        return 'Voice!'


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

print(dog.voice())
print(cat.voice())
print(cow.voice())
