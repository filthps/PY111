"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx


root = {
    "key": 8,
    "value": 8,
    "left": {
        "key": 8,
        "value": 8,
        "left": None,
        "right": None
    },
    "right": {
        "key": 8,
        "value": 8,
        "left": None,
        "right": None
    }
}


class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def create_node(key, value, left: Optional[dict] = None, right: Optional[dict] = None):
        return {
            "key": key,
            "value": value,
            "left": left,
            "right": right
        }

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self.create_node(key, value)
        else:
            current = self.root
            while True:
                current_key = current["key"]
                if current_key > key:
                    right_node = current["right"]
                    if right_node is None:
                        current["right"] = self.create_node(key, value)
                        break
                    else:
                        current = current["right"]
                        current["right"] = self.create_node(key, value)
                        break
                else:
                    left_node = current["left"]
                    if left_node is None:
                        current["left"] = self.create_node(key, value)
                        break
                    else:
                        current = current["left"]
                        current["left"] = self.create_node(key, value)

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
        def find_key(current_node):
            if current_node is None:
                raise KeyError
            current_key = current_node["key"]
            if current_key == key:
                return current_node["value"]
            next_node = current_node["left"] if key < current_key else current_node["right"]
            find_key(next_node)
        return find_key(key)

    def generator(self):
        current = self.root
        if current is None:
            return
        left = current.left
        right = current.right
        while left or right:
            left = current.left
            right = current.right
            yield (left, right,)

    def __iter__(self):
        return self.generator()

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None
