﻿N = int(input("Введите число N: "))
if N <= 0 or N >100000:
    print("Ошибка, недопустимое число!")
else:
    B = list(map(int,input("Через пробел введите числа в количестве, равному числу N: ").split()))
    if len(B) != N:
        print("Ошибка, количество введенных чисел не равно N!")
    else:
        count = len(set(B))
        print("Количество уникальных чисел: ", count)


