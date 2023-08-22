from repository import RedBlackTreeRepository


class RedBlackTreeController:
    def __init__(self):
        self.rbt_controller = RedBlackTreeRepository()

    def start(self):
        flag = True
        while flag:
            print(
                """
                =========================================================
                Красно-чёрное дерево создано! Выберите следующее действие
                1. Добавить элемент
                2. Добавить N произвольных элементов от 0 до 100
                3. Проверить элемент на наличие
                4. Удалить элемент
                5. Вывести дерево
                6. Завершить программу
                =========================================================
                """)
            input_user = int(input('-> '))
            match input_user:
                case 1:
                    value_insert = int(input('Что добавить? -> '))
                    self.rbt_controller.insert_node(value_insert)
                case 2:
                    amount_insert = int(input('Сколько добавить? -> '))
                    self.rbt_controller.insert_multiple(amount_insert)
                case 3:
                    find_node = int(input('Что найти? -> '))
                    self.rbt_controller.find_node(find_node)
                case 4:
                    delete_node = int(input('Что удалить? -> '))
                    self.rbt_controller.delete_node(delete_node)
                case 5:
                    self.rbt_controller.print_tree()
                case 6:
                    flag = False
                    print('Bye!')
                case _:
                    print('Неправильно, попробуй ещё раз')
                    pass
