"""Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль."""

number_1 = int(input("Введите целое первое число: "))
number_2 = int(input("Введите целое второе число: "))


def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print("На 0 делить нельзя!")


print(division(number_1, number_2))
