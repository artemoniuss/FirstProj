#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = []
for i in garden:
    if not garden_set.__contains__(i):
        garden_set.append(i)
print(garden_set)
meadow_set = []
for i in meadow:
    if not meadow_set.__contains__(i):
        meadow_set.append(i)
print(meadow_set)
# выведите на консоль все виды цветов
# TODO здесь ваш код
all_set = []
for i in garden:
    if not all_set.__contains__(i):
        all_set.append(i)
for i in meadow:
    if not all_set.__contains__(i):
        all_set.append(i)
print(all_set)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
cross_set = []
for i in garden_set:
    if meadow_set.__contains__(i):
        cross_set.append(i)
print(cross_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
cross_gar_set = []
for i in garden_set:
    if not meadow.__contains__(i):
        cross_gar_set.append(i)
print(cross_gar_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
cross_mea_set = []
for i in meadow_set:
    if not garden.__contains__(i):
        cross_mea_set.append(i)
print(cross_mea_set)
