#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
# добавьте птиц из списка birds в последние клетки зоопарка
#  и выведите список на консоль
# TODO здесь ваш код
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)
birds = ['rooster', 'ostrich', 'lark', ]
zoo += birds
print(zoo)
zoo.remove('elephant')
print(zoo)
for i in range(0, len(zoo)):
    if zoo[i] == 'lion':
        print(f"Лев в клетке под номером - { i + 1 }")
    if zoo[i] == 'lark':
        print(f"Жаворонок в клетке под номером - {i + 1}")