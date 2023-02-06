"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(var_1, var_2, var_3):
    if var_1 < var_2:
        if var_1 < var_3:
            return var_2 + var_3
        else:
            return var_1 + var_2
    elif var_2 > var_3:
        return var_1 + var_2
    else:
        return var_1 + var_3

number_1 = int(input("Введите целое первое число: "))
number_2 = int(input("Введите целое второе число: "))
number_3 = int(input("Введите целое третье число: "))

print(my_func(number_1, number_2, number_3))

