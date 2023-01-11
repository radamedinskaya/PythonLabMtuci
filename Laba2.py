import random
import sys
import time
from bisect import bisect_left

array = []

# Создаем двоичное дерево поиска
def findMaximumKey(ptr):
    while ptr.right:
        ptr = ptr.right
    return ptr


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Функция добавления элемента
    def addElement(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.addElement(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.addElement(value)
        else:
            self.value = value

    # Функция вывода элементов в консоль
    def showElements(self):
        if self.left:
            self.left.showElements()
        print(self.value),
        if self.right:
            self.right.showElements()

    def makelist(self):
        if self.left:
            self.left.makelist()
        array.append(self.value),
        if self.right:
            self.right.makelist()


    # Функция удаления элемента
    def deleteElement(self, value):
        if self is None:
            return self

        if value < self.value:
            self.left = self.left.deleteElement(value)

        elif value > self.value:
            self.right = self.right.deleteElement(value)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left and self.right:
                pre = self.left.findMaximumKey(self.left)
                self.value = pre
                self.left = self.left.deleteNode(pre)
            else:
                child = self.left if self.left else self.right
                self.value = child
        return self

    # Функция поиска элемента
    def lookForElement(self, value):
        if self is None:
            print("Пустая структура")
        elif value < self.value:
            return self.left.lookForElement(value) if self.left else print("Элемент не найден")
        elif value > self.value:
            return self.right.lookForElement(value) if self.right else print("Элемент не найден")
        else:
            print("Элемент найден")


if __name__ == "__main__":
    # array1 = input("Введите элементы массива:").split()
    num = int(input("Введите количество элементов массива:"))
    sampleClass = Node()
    # Заполнение случайными числами
    for i in range(num):
        sampleClass.addElement(random.randint(0, 1000))
    #sampleClass.showElements()
    works = True
    while works:
        op = int(input("Выберите операцию: \n1. Добавить элемент\n2. Удалить элемент\n3. Поиск элемента\n4. Завершение "
                       "программы\n"))
        if op == 1:
            add = int(input("Введите значение для добавления: "))
            sampleClass.addElement(add)
            #sampleClass.showElements()
            sampleClass.makelist()
        elif op == 2:
            delete = int(input("Введите значение для удаления: "))
            sampleClass.deleteElement(delete)
            #sampleClass.showElements()
            sampleClass.makelist()
        elif op == 3:
            sampleClass.makelist()
            search = int(input("Введите значение для поиска: "))
            start_time = time.time()
            sampleClass.lookForElement(search)
            esttime = round((time.time() - start_time) * 1000, 3)
            start_time_auto = time.time()
            i = bisect_left(array, search)
            print("Элемент найден") if i != len(array) and array[i] == search else print("Элемент не найден")
            esttime_auto = round((time.time() - start_time) * 1000, 3)
            print("Бинарное дерево: " + str(esttime) + "\nАвтоматический поиск: " + str(esttime_auto))
        elif op == 4:
            works = False
        else:
            print("Введите значение в диапазоне от 1 до 3")

    sys.exit()

