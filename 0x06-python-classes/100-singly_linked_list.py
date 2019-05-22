 #!/usr/bin/python3


class Node:
    """ Model of Node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Model of single linked list use Node class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            aux = self.__head
            if value <= aux.data:
                self.__head = Node(value, aux)
            else:
                while(aux.next_node is not None):
                    if (aux.next_node.data >= value):
                        new_node = Node(value, aux.next_node)
                        aux.next_node = new_node
                        break
                    else:
                        aux = aux.next_node
                if aux.next_node is None:
                    aux.next_node = Node(value)

    def __str__(self):
        aux = self.__head
        str = ""
        while(aux is not None):
            if (aux.next_node is not None):
                str = "{}{:d}\n".format(str, aux.data)
            else:
                str = "{}{:d}".format(str, aux.data)
            aux = aux.next_node
        return str
