"""
5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

from time import perf_counter
import random

src = [random.randint(1, 2000) for _ in range(1, 10001)]
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(src)

# Первый способ поиска уникальных элементов списка
start = perf_counter()
unique_num_1 = [el for el in src if src.count(el) == 1]
print(unique_num_1, '\n', type(unique_num_1), perf_counter() - start, 'sec')

# Второй способ с применением множеств для поиска элемента
# При увеличении размера списка данный способ значительно сокращает время на операцию
start = perf_counter()
src_set_uni, tmp = set(), set()
for el in src:
    if el not in tmp:
        src_set_uni.add(el)
    else:
        src_set_uni.discard(el)
    tmp.add(el)
src_res = [num for num in src if num in src_set_uni]
print(src_res, '\n', type(src_res), perf_counter() - start, 'sec')
