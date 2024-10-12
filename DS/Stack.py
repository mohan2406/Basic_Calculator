from typing import Any

from DS.Node import Node


# Python class to implement stack data structure

class Stack:
    def __init__(self):
        self.__top = None
        self.__count = 0

    def push(self, data: Any):
        down = self.__top
        self.__top = Node(data, down)
        self.__count += 1

    def pop(self) -> Any:
        try:
            element = self.__top.get_data()
            self.__top = self.__top.next_node()
            self.__count -= 1
            return element
        except (IndexError, AttributeError):
            print("\033[31m Trying to perform pop operation in empty stack! \033[0m")

    def peek(self) -> Any:
        try:
            return self.__top.get_data()
        except AttributeError:
            print("\033[31m Trying to get element from empty stack! \033[0m")

    def count(self) -> int:
        return self.__count

    def is_empty(self) -> bool:
        if self.__count == 0:
            return True
        else:
            return False


# test code

if __name__ == '__main__':
    s = Stack()
    print('s = ', s)
    s.push('5')
    s.push('6')
    print('nodes count = ', s.count())
    print('top = ', s.peek())
    print('popped element = ', s.pop())
    print('top = ', s.peek())
    print('is empty = ', s.is_empty())
    print('nodes count = ', s.count())
    print('popped element = ', s.pop())
    print('nodes count = ', s.count())
    print('top = ', s.peek())
    print('is empty = ', s.is_empty())
    print(s.pop())  # this will raise index error
    print(s.pop())
