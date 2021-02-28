"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
1
# >>> next(odd_to_15)
3
...
# >>> next(odd_to_15)
15
# >>> next(odd_to_15)
...StopIteration...
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""

n = 20


def odd_nums(i):
    for num in range(1, i + 1, 2):
        yield num


# Первый способ (с помощью функции с yield)
nums_gen_1 = odd_nums(n)
print(type(nums_gen_1))
print(*nums_gen_1)

# С помощью генераторного выражения
nums_gen_2 = (num for num in range(1, n + 1) if num % 2 != 0)
print(type(nums_gen_2))
print(*nums_gen_2)

