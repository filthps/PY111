from typing import List


def sort(container: List[int]) -> List[int]:
    for index in range(len(container)):
        item = container[index]
        try:
            item_1 = container[index + 1]
        except IndexError:
            item_1 = None
        if item_1 is not None:
            print(item, item_1)
            if item_1 < item:
                container[index], container[index + 1] = item_1, item
    return container


if __name__ == "__main__":
    print([100, -2, 5, 4, 54, -34], sort([100, -2, 5, 4, 54, -34]))
