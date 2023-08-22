import random
from avl_tree import AVLTree


class AVLTreeRemote:
    def __init__(self):
        self.AVLTree = AVLTree()

    def insert_node(self, value: int):
        self.AVLTree.insert(value)

    def insert_multiple(self, amount: int):
        for i in range(amount):
            self.AVLTree.insert(random.randint(0, 100))

    def find_node(self, value: int):
        print(self.AVLTree.find(value))

    def delete_node(self, value: int):
        self.AVLTree.delete(value)

    def print_tree(self):
        print(self.AVLTree)
