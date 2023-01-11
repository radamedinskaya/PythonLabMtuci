import time
import random

# Встроенная функция сортировки sort
def Default(array):
    start_time = time.time()
    array.sort()
    return round((time.time() - start_time) * 1000, 3)


# Алгоритм быстрой сортировки
def QuickSort(array, start, end):
    start_time = time.time()
    if end - start > 1:
        p = partition(array, start, end)
        QuickSort(array, start, p)
        QuickSort(array, p + 1, end)
        return round((time.time() - start_time) * 1000, 3)


def partition(array, start, end):
    pivot = array[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and array[i] <= pivot:
            i = i + 1
        while i <= j and array[j] >= pivot:
            j = j - 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[start], array[j] = array[j], array[start]
            return j


# Сортировка вставками
def Insertion(array):
    start_time = time.time()
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return round((time.time() - start_time) * 1000, 3)


if __name__ == "__main__":
    # array1 = input("Введите элементы массива:").split()
    # print(array1)
    num = int(input("Введите количество элементов массива:"))
    array1 = [random.randint(0, 100000) for i in range(num)]
    array2 = array3 = array1[:]
    print("Стандартная сортировка: " + str(Default(array1)) + "ms\nБыстрая сортировка: " + str(QuickSort(array2, 0, len(array2))) + "ms\nСортировка вставками: " + str(Insertion(array3)) + "ms")

