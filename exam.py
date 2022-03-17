from typing import  Iterable
from random import  randint
from itertools import cycle
from collections import deque

#1)

a = len(arr) - 1  # O(1) + O(1)
out = list()  # O(1)
while a > 0:  # O(log1.7(n))
    out.append(arr[a])  # O(1) + O(1)
    a = a // 1.7  # O(1)
out.merge_sort()  # O(log1.7(n) * log2(n))

# g(n) = 1 + 1 + 1 + log1.7() + 1 + 1 + 1 + log1.7(n) * log2(n)
# g(n) = 3 + log1.7() + 3 + log1.7(n) * log2(n)
# f(n) = log1.7(n) * log2(n)

#2)

# Итеративная реализация
words = 10
n = [1,2,3,4]
equeue = cycle(n)  # Люди (очередь)
while len(n) > 1:  #O(n - 1)
    for k in range(words):  # K Слоги O(k)
        i = next(equeue)  #O(1)
        if k == words - 1:  # O(1)
            n.remove(i) # O(n) + O(n)

# f(g) = n - 1 * (k * (1 + 1 + 2n))
# f(g) = n * k * n
# f(n) = n**

# Рекурсивная реализация
words = 10
n = [1,2,3,4]
equeue = cycle(n)  # Люди (очередь)
def start():
    for k in range(words):  # K Слоги O(k)
        i = next(equeue)  #O(1)
        if k == words - 1:  # O(1)
            n.remove(i)  # O(n) + O(n)
            if len(n) > 1:  # Базовый случай
                return start()
            else:
                return n[0]  # Победитель

if n:  # Базовый случай
    start()  # O(n - 1)

# f(g) = n - 1 * (k * (1 + 1 + 2n))
# f(g) = n * k * n
# f(n) = n**


words = 10
n = [1,2,3,4]
equeue = deque(n)

while len(equeue) > 1:
    for k in range(words):  # O(n)
        i = equeue.pop()  # O(1)
        if k < words - 1:  # O(1)
            equeue.push(i)  # O(1)




# 4)
arr = {i: randint(1, 10) for i in range(100)}




# 6)

def count_per_day(orders):
    def count_all_orders(ord_: list[tuple]) -> Iterable[set]:
        return map(lambda x: set(range(*x)), ord_)  # O(n) * (O(1) * O(k))

    def get_intersections(times: Iterable[set]):
        return set.intersection(*times)  # O(n) + O(k)

    busy_times = count_all_orders(orders)
    overlay_time = get_intersections(busy_times)
    return not bool(overlay_time)


orders_ = [(0, 14), (2, 11), (17, 20)]
status = count_per_day(orders_)  # status - True/False (Хватает ли нам 1 ракеты)

# g(n) = O(n) * (O(1) * O(k)) + O(n) + O(k)
# f(n) = O(n * k)

# 7)
