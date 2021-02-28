"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию кода по памяти,
 по скорости.
"""

from time import perf_counter
import sys

# List Comprehensions
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_l = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(res_l, '\n', type(res_l), sys.getsizeof(res_l), 'byte,', perf_counter() - start, 'sec')

# Generator
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_l = (src[i] for i in range(1, len(src)) if src[i] > src[i-1])
print(*res_l, '\n', type(res_l), sys.getsizeof(res_l), 'byte,', perf_counter() - start, 'sec')

