# Class used to create node

class Node:
    def __init__(self, data, next_node=None):
        self.__Data = data
        self.__Next = next_node

    def get_data(self):
        return self.__Data
    
    def next_node(self):
        return self.__Next

    def set_data(self, data):
        self.__Data = data

    def set_next(self, next_node):
        if isinstance(next_node, Node) or (next_node is None):
            self.__Next = next_node
    

# test code
if __name__ == '__main__':
    a = Node(3, None)

    print(a.get_data())
    print(a.next_node())

    b = Node(5, a)

    print(b.get_data())
    print(b.next_node())

    print(a)

    b = b.next_node()
    print(b.get_data())
    print(b.next_node())
    print(b)
