from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left-border = 0
    rigth-border = len(arr) - 1

    while left_border <= right_border:
        middle_index = left_border + (right_border - left_border) // 2
        middle_val = arr[middle_index]
        if elem == middle_val:
            return arr[elem]
        elif elem < middle_index:
            right_border = middle_index - 1
        elif elem > middle_index:
            left_border = middle_index + 1
        return None
