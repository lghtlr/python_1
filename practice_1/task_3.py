# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = float(input("Ваш вес в кг: "))
height = float(input("Ваш рост в см: "))/100


#Ваш кол
#TODO: перевела см в м, г в кг
body_mass_index = weight/height**2

print(body_mass_index)
