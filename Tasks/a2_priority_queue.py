"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        """
        Начало слева
        Конец справа
        """
        self.queue = {}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        queue = self.queue.get(priority, None)
        if queue is None:
            self.queue[priority] = [elem]
        else:
            queue.append(elem)

        # queue = self.queue.get(priority, [])
        #
        # queue.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.queue:
            return None
        key = min(self.queue)
        queue = self.queue[key]
        if queue:
            val = queue.pop(0)
            if not len(queue):
                del self.queue[key]
            return val

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        queue = self.queue.get(priority, None)
        if queue is None:
            return None
        if len(queue) <= ind:
            return None
        val = queue[ind]
        return val

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue = {}
        return None
