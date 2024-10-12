from typing import Any

from DS.Node import Node


# Python class to implement queue data structure

class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__count = 0

    def enqueue(self, data: Any):
        if self.__count == 0:
            self.__front = self.__rear = Node(data)
            self.__count = 1
        else:
            prev = self.__rear
            self.__rear = Node(data)
            prev.set_next(self.__rear)
            self.__count += 1

    def dequeue(self) -> Any:
        try:
            element = self.__front.get_data()
            self.__front = self.__front.next_node()
            if self.__front is None:
                self.__rear = None
            self.__count -= 1
            return element
        except (IndexError, AttributeError):
            print("\033[31m Trying to perform pop operation in empty queue! \033[0m")

    def peek(self) -> Any:
        try:
            return self.__front.get_data()
        except AttributeError:
            print("\033[31m Trying to get element from empty queue! \033[0m")

    def count(self) -> int:
        return self.__count

    def is_empty(self) -> bool:
        if self.__count == 0:
            return True
        else:
            return False

    def find(self, data: Any) -> int:
        try:
            ptr = self.__front
            index = 0
            if ptr.get_data() == data:
                return index
            while ptr.next_node() is not None:
                if ptr.get_data() == data:
                    return index
                ptr = ptr.next_node()
                index += 1
            print("\033[93m'{}' element not found in the queue. \033[0m".format(data))
        except AttributeError:
            print("\033[31m Trying to find element in an empty queue! \033[0m")


# test code

if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(9)
    print("nodes count = ", q.count())
    print("index of 6 = ", q.find(6))
    print('peek = ', q.peek())
    print('dequeue element = ', q.dequeue())
    print('peek = ', q.peek())
    print('is empty = ', q.is_empty())
    print('nodes count = ', q.count())
    print('index of 6 = ', q.find(6))
    print('index of q = ', q.find(q))
    print('dequeue element = ', q.dequeue())
    print('peek = ', q.peek())
    print('nodes count = ', q.count())
    print('dequeue element = ', q.dequeue())
    print('peek = ', q.peek())
    print('is empty = ', q.is_empty())
    print('nodes count = ', q.count())
    print('index of 4 = ', q.find(4))
