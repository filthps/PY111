"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx


class Elem:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.__left = left
        self.__right = right

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value: Optional["Elem"]):
        self.__right = value
        
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, value):
        self.__left = value

    def __repr__(self):
        return f"{type(self)}({self.key, self.value})"

    def __str__(self):
        return str(self.value)
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def create_node(key, value, left: Optional[dict] = None, right: Optional[dict] = None):
        return Elem(key, value, left, right)

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
            current_key = current.key
            if current_key > key:
                right_node = current.right
                if right_node is None:
                    current.right = self.create_node(key, value)
                    return
                else:
                    current = current.right
                    current.right = self.create_node(key, value)
                    return
            else:
                left_node = current.left
                if left_node is None:
                    current.left = self.create_node(key, value)
                    return
                else:
                    current = current.left
                    current.left = self.create_node(key, value)

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        try:
            node = self.find(key)
        except KeyError:
            node = None
        if node is not None:
            pass

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        def find_key(current_node):
            if type(current_node) is int:
                current_node = self.root
            if current_node is None:
                raise KeyError
            current_key = current_node.key
            print(current_key, key)
            if current_key == key:
                return current_node.value
            next_node = current_node.left if key < current_key else current_node.right
            return find_key(next_node)
        return find_key(key)

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None
