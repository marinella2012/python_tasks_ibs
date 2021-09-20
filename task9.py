# Необходимо создать два параллельных потока, каждый из которых
# выводил бы на экран числа от 10 до 1 в обратном порядке синтервалом в
# одну секунду. В выводе должно быть понятно какая нить выполняется,
# и когда каждая из них начинает и заканчивает своё выполнение.
import threading
import time

class TwoFlows:
    def __init__(self, index):
        self.index = index

    def go(self):
        for index in reversed(range(1, 11)):
            time.sleep(1)
            print(f'{index}\n')

flows = TwoFlows(2)

for i in range(2):
    t = threading.Thread(target=flows.go)
    t.start()
