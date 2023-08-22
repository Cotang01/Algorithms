from repository import AVLTreeRemote
AVLTreeRemote = AVLTreeRemote()


def start():
    global AVLTreeRemote  # тестовая реализация
    flag = True
    while flag:
        print(
            """
            ================================================
            АВЛ Дерево создано! Выберите следующее действие
            1. Добавить элемент
            2. Добавить N произвольных элементов от 0 до 100
            3. Проверить элемент на наличие
            4. Удалить элемент
            5. Вывести дерево
            6. Завершить программу
            ================================================
            """)
        input_user = int(input('-> '))
        match input_user:
            case 1:
                value_insert = int(input('Что добавить? -> '))
                AVLTreeRemote.insert_node(value_insert)
            case 2:
                amount_insert = int(input('Сколько добавить? -> '))
                AVLTreeRemote.insert_multiple(amount_insert)
            case 3:
                find_node = int(input('Что найти? -> '))
                AVLTreeRemote.find_node(find_node)
            case 4:
                delete_node = int(input('Что удалить? -> '))
                AVLTreeRemote.delete_node(delete_node)
            case 5:
                AVLTreeRemote.print_tree()
            case 6:
                flag = False
                print('Bye!')
            case _:
                print('Неправильно, попробуй ещё раз')
                pass
