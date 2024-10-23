#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Mother", "Father", "Sister"]
my_family_height = [
    # ['имя', рост],
    [my_family[0], 178],
    [my_family[1], 189],
    [my_family[2], 167],
]
for i in my_family_height:
    if i[0] == "Father":
        print(f"Рост отца - {i[1]} см")
summ = 0
for i in my_family_height:
    summ += i[1]
print(summ / len(my_family_height))