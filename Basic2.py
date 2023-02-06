"""Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой."""

my_first_name = input("Введите свое имя: ")
my_last_name = input("Введите свою фамилию: ")
my_birth_year = int(input("Введите год своего рождения: "))
my_city = input("Введите свой город: ")
my_email = input("Введите свою электронную почту: ")
my_phone = input("Введите свой номер телефона: ")


def data_processing(first_name='-', last_name='-', birth_year=None, city='-',
                    email='-', phone='-'):
    print(f'Данные пользователя следующие: имя - {first_name}, фамилия - '
          f'{last_name}, год рождения - {birth_year}, город проживания - '
          f'{city}, почта - {email}, телефон - {phone}.')

data_processing(first_name=my_first_name, last_name=my_last_name, birth_year=
my_birth_year, city=my_city, email=my_email, phone=my_phone)
