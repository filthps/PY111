from typing import List
from itertools import chain


def sort(container: List[int]):
    result = []
    raw_left = []
    raw_right = []

    def slice_(left_sec, right_sec):


    if len(container) > 1:  # Базовый случай
        raw_left = slice_(container[:len(container) // 2], container[len(container) // 2:])
        print(raw_left)
    else:
        return container
    return


if __name__ == "__main__":
    print(sort([33, 6, 1, 343, 10]))
