from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    def lazy_stairway_path(num):
        """Рекурсивная функция, которая возвращает стоимость до N-ступени"""
        total_coast = {}
        if num == 0 or num == 1:
            total_coast.update({num: stairway[num]})
            return stairway[num]
        current_price = total_coast.get(num, None)
        if current_price is None:
            current_price = stairway[num] + min(lazy_stairway_path(num - 1), lazy_stairway_path(num - 2))
            total_coast.update({num: current_price})
        return current_price

    return lazy_stairway_path(len(stairway) - 1)


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """Прямой метод"""
    count = len(stairway)
    total_coast = [float("inf")] * count  # стоимость перемещения по ступеням
    total_coast[0] = stairway[0]  # Начальные условия
    total_coast[1] = min(stairway[1], stairway[0] + stairway[1])  # нвчальные условия для первой ступени

    for i in range(2, count):
        total_coast[i] = stairway[i] + min(total_coast[i - 1], total_coast[i - 2])
    return total_coast[-1]

def reversed_direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """ Обратный метод """
    count = len(stairway)
    total_coast = [float("inf")] * count  # стоимость перемещения по ступеням
    total_coast[0] = stairway[0]  # начальные условия первой ступени
    total_coast[1] = stairway[1]  # начальные условия второй ступени

    for i in range(0, count - 2):
        total_coast[i + 1] = min(total_coast[i + 1], stairway[i + 1] + total_coast[i])
        total_coast[i + 2] = min(total_coast[i + 2], stairway[i + 2] + total_coast[i])
    total_coast[-1] = min(total_coast[-1], stairway[-1] + total_coast[-2])

    return total_coast[-1]
