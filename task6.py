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
        return ('Гав!')


class Car(Animal):

