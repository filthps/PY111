"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple, Union, Iterator
from random import randint, choice
import networkx as nx


class Node:
    def __init__(self, key: int, val: Any, left: Optional["Node"] = None, right: Optional["Node"] = None):
        if not type(key) is int:
            raise TypeError
        self.__key = key
        self.value = val
        self.__left = left
        self.__right = right

    def get_key(self):
        return self.__key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        self.is_valid(node)
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        self.is_valid(node)
        self.right = node

    @staticmethod
    def is_valid(k):
        if not isinstance(k, Node):
            raise TypeError

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__key},{self.value})"


class BinarySearchTree:
    def __init__(self, items: Iterator[dict]):
        self.head = None
        prev_node = Node
        for key, val in items.items():
            node = Node(key, val)
            if self.head is None:
                self.head = node
                prev_node = node
            else:
                if prev_node.get_key() <= key:
                    prev_node.right = node
                else:
                    prev_node.left = node
                prev_node = node

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        print(key, value)
        return None

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        return None

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None


if __name__ == "__main__":
    def gen_items(len_: int):
        k = ("retdfg", "323", 6, "fgdfb", 342, 5,)
        keys = map(lambda a: randint(0, a),  range(len_))

        def gen_d():
            while True:
                try:
                    key = next(keys)
                except StopIteration:
                    return
                yield {key: choice(k)}
        return gen_d()
    BinarySearchTree(gen_items(222))
