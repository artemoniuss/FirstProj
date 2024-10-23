#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distances = {}
for i in sites:
    distances[i] = {}
    for j in sites:
        if i != j:
            x1, y1 = sites[i]
            x2, y2 = sites[j]
            distances[i][j] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# TODO здесь заполнение словаря

print(distances['Moscow']['Paris'])




