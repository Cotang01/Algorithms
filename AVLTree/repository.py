import random
from avl_tree import AVLTree


class AVLTreeRemote:
    def __init__(self):
        self.avl_tree = AVLTree()

    def insert_node(self, value: int):
        self.avl_tree.insert(value)

    def insert_multiple(self, amount: int):
        for i in range(amount):
            self.avl_tree.insert(random.randint(0, 100))

    def find_node(self, value: int):
        print(self.avl_tree.find(value))

    def delete_node(self, value: int):
        self.avl_tree.delete(value)

    def print_tree(self):
        print(self.avl_tree)
