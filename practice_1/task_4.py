# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""
# TODO: нужно ли проверять вход на валидность?
number = input("Введите целое четырехзначное число:")
sum = 0
if int(number) < 1000 or int(number) > 9999:
    print("Вы ввели неверные данные!")
else:
    for digit in number:
        sum += int(digit)
    print(sum)