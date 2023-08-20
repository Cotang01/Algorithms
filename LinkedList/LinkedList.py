
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def find(self, value: int):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return current
                current = current.next
            return None

    def add_end(self, value: int):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_start(self, value: int):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, value: int):
        if self.is_empty():
            return None
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next
            if self.head is not None:
                self.head.prev = None
        else:
            while current_node is not None:
                if current_node.value == value:
                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev
                    current_node.prev.next = current_node.next
                current_node = current_node.next

    def insert_after(self, value: int, node: Node):
        next_node = node.next
        new_node = Node
        new_node.value = value
        node.next = new_node
        new_node.prev = node
        if next_node is None:
            self.tail = new_node
        else:
            next_node.prev = new_node
            new_node.next = next_node

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next
        return ', '.join(nodes)


my_list = LinkedList()
my_list.add_end(10)
my_list.add_end(20)
my_list.add_end(30)
my_list.add_end(40)
my_list.add_end(50)
my_list.add_start(5)
my_list.add_start(12)
my_list.delete(5)
print(my_list)
print(my_list.find(20))