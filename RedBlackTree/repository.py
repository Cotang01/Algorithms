import random
from red_black_tree import RedBlackTree


class RedBlackTreeRepository:
    def __init__(self):
        self.red_black_tree = RedBlackTree()

    def insert_node(self, value: int):
        self.red_black_tree.insert(value)

    def insert_multiple(self, amount: int):
        for i in range(amount):
            self.red_black_tree.insert(random.randint(0, 100))

    def find_node(self, value: int):
        print(self.red_black_tree.find(value))

    def delete_node(self, value: int):
        self.red_black_tree.delete(value)

    def print_tree(self):
        print(self.red_black_tree)
