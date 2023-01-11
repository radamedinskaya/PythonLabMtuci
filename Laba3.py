import sys
import time

string = ""


# Вычисляем префикс
def prefix(suffix):
    pref = [0] * len(suffix)
    for i in range(1, len(suffix)):
        j = pref[i - 1]
        while suffix[j] != suffix[i] and j > 0:
            j = pref[j - 1]
        if suffix[j] == suffix[i]:
            j = j + 1
        pref[i] = j
    return pref


# Поиск подстроки методом Кнута-Морриса-Пратта
def findSubstring(suffix, text):
    index = -1
    f = prefix(suffix)
    k = 0
    for i in range(len(text)):
        while k > 0 and suffix[k] != text[i]:
            k = f[k - 1]
        if suffix[k] == text[i]:
            k = k + 1
        if k == len(suffix):
            index = i - len(suffix) + 1
            break
    return index


if __name__ == "__main__":
    string = input("Введите строку: ")
    works = True
    while works:
        op = int(input("Выберите операцию: \n1. Ввести подстроку\n2. Найти подстроку\n3. Новая строка\n4. Завершение "
                       "программы\n"))
        if op == 1:
            newstr = input("Введите подстроку: ")
            string += newstr
            print("Полученная строка: " + string + "\nВведенная подстрока: " + newstr)
        elif op == 2:
            option = input("Учитывать регистр? (1 - да, 2 - нет)\n")
            sub = input("Введите подстоку для поиска: ")
            if int(option) == 2:
                str1 = string.lower()
                str2 = sub.lower()
            else:
                str1 = string
                str2 = sub
            start_time = time.time()
            findSubstring(str2, str1)
            esttime = round((time.time() - start_time) * 1000, 3)
            print("Подстрока найдена - " + str(esttime) + " мс") if findSubstring(str2, str1) != -1 \
                else print("Подстрока не найдена - " + str(esttime) + " мс")
            start_time = time.time()
            str1.find(str2)
            esttime_auto = round((time.time() - start_time) * 1000, 3)
            print("Подстрока найдена - " + str(esttime_auto) + " мс") if str1.find(str2) != -1 \
                else print("Подстрока не найдена - " + str(esttime_auto) + " мс")
        elif op == 3:
            string = input("Введите новую строку: ")
            print("Новая строка: " + string)
        elif op == 4:
            works = False
        else:
            print("Введите значение в диапазоне от 1 до 3")

    sys.exit()
