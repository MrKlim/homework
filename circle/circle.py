#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.

from math import pi
def perimeter(diameter):
    diameter = pi * diameter
    if diameter > 0:
        return diameter
    else:
        print('Нужна сковородка побольше')


def square(diameter):
    t = pi * (diameter / 2) ** 2
    if diameter > 0:
        return t
    else:
        print('Нужна сковородка побольше')
