
# создаём класс узла
class Node:
    # для инициализации достаточно передать value
    def __init__(self, value: int, left=None, right=None):
        self.value = value  # значение
        self.left = left  # левый потомок
        self.right = right  # правый потомок
        self.height = 0  # высота элемента

    # при переводе в строку выводим его value, нижний и левый элемент
    def __str__(self):
        return f'{self.value}, левый {self.left}, правый {self.right}'


# создаём класс дерева
class AVLTree:
    # при инициализации создаётся root, который будет являться корнем дерева
    def __init__(self, root=None):
        self.root = root

    # метод поиска элемента по значению
    def find(self, value: int) -> Node:
        return self._find_assist(self.root, value)

    '''
    Вспомогательная функция поиска элемента по значению нужна, чтобы 
    поиск был возможен при условии принятия только значения искомого элемента
    то есть чтобы не требовалось дополнительных данных для получения результата
    '''
    # вспомогательная рекурсивная функция
    def _find_assist(self, current: Node, value: int):
        if current is None:  # если нет такого элемента, возвращаем None
            return None
        elif current.value == value:  # если элемент нашёлся, возвращаем его
            return current
        elif current.value > value:  # если элемент больше значения, то идём
            return self._find_assist(current.left, value)  # влево по дереву
        elif current.value < value:  # если элемент больше значения, то идём
            return self._find_assist(current.right, value)  # вправо по дереву

    '''
    При реализации метода вставки я хотел, чтобы функция принимала только 
    значение, а затем уже сама добавляла нод там, где это нужно исходя из 
    критериев дерева (меньшие значения слева, большие - справа)
    В одной функции не удаётся удовлетворить все требования из-за особенности
    рекурсии, поэтому она делится на 2 функции, 1 из которых рекурсивна
    '''

    def insert(self, value: int) -> None:  # если дерево пустое, то первый
        if self.root is None:      # добавляемый элемент становится корнем
            self.root = Node(value)
        else:                      # в противном случае запускается
            self._insert_assist(self.root, value)  # вспомогательная рекурсия

    def _insert_assist(self, current: Node, value: int) -> None:
        if current.value > value:  # если новое значение меньше узла
            if current.left is None:  # и если место слева от него свободно,
                current.left = Node(value)  # то ставим значение туда
            else:  # в противном случае ищем свободное место дальше, передавая
                # передавая в рекурсию левый узел
                if current is not None:
                    self._update_height(current)
                    self._balance(current)
                self._insert_assist(current.left, value)
        if current.value < value:  # и так же, если новое значение больше узла
            if current.right is None:
                current.right = Node(value)
            else:  # только передаётся уже правый узел
                if current is not None:
                    self._update_height(current)
                    self._balance(current)
                self._insert_assist(current.right, value)

    '''
    К удалению у меня были те же требования - дай value, получи result.
    Удаление происходит по следующему принципу:
    
    1) Если у удаляемого элемента 0 или 1 потомок, то элемент перенимает либо
    None, либо значение имеющегося потомка соответственно.
    2) Если у удаляемого элемента 2 потомка, то он перенимает либо значение
    максимального элемента слева от себя, либо значение минимального элемента
    справа от себя (на выбор), а затем элемент с заимствованными значением 
    рекурсивно удаляется
    '''

    def delete(self, value: int) -> None:
        return self._delete_assist(self.root, value)
        # передаём во вспомогательную рекурсию root и значение для удаления

    def _delete_assist(self, del_node: Node, value: int):
        if del_node is None:  # если такого узла нет, возвращается None
            return None
        # алгоритм поиска удаляемого узла аналогичный _find_assist()
        elif del_node.value > value:
            del_node.left = self._delete_assist(del_node.left, value)
        elif del_node.value < value:
            del_node.right = self._delete_assist(del_node.right, value)
        else:
            if del_node.left is None:  # если нет левого потомка, то на место
                del_node = del_node.right  # узла встаёт его правый потомок
            elif del_node.right is None:  # и наоборот
                del_node = del_node.left
            else:
                """
                Если у узла есть 2 потомка, то (в данном примере) находим
                минимальный элемент справа от узла, который встанет на его
                место.
                Передаём значение.
                Рекурсивно удаляем элемент, от которого перенималось значение.
                """
                node_max_right = self._find_min(del_node.right)
                del_node.value = node_max_right.value
                del_node.right = self._delete_assist(del_node.right,
                                                     node_max_right.value)
        if del_node is not None:
            self._update_height(del_node)
            self._balance(del_node)
        return del_node

    # функция поиска минимального значения
    def _find_min(self, node: Node) -> Node:
        if node is None:
            return None
        if node.left is None:
            return node
        return self._find_min(node.left)

    # функция поиска максимального значения
    def _find_max(self, node: Node) -> Node:
        if node is None:
            return None
        if node.right is None:
            return node
        return self._find_min(node.right)

    '''
    Балансировка дерева.
    Для того, чтобы наше дерево было сбалансированным (чтобы сложность 
    поиска и вставки всегда была O(log(n))), надо контролировать высоту 
    каждого узла, делать это придётся после каждого добавления или удаления
    элемента.
    Разница высоты для каждого дочернего узла должна быть не больше |1| 
    (высота узла это самый длинный путь от его потомка до самого нижнего листа)
    У None будет высота -1
    У листа будет высота 0 и т.д.
    '''

    # функция обновления высоты ноды
    def _update_height(self, node: Node):
        height = max(self._get_height(node.left),
                     self._get_height(node.right)) + 1
        return height

    # функция получения высоты ноды, для несуществующих это -1, для самых
    # низких это 0 и +1 при каждом вызове рекурсии при вставке или удалении
    def _get_height(self, node: Node) -> int:
        if node is None:
            return -1
        else:
            return node.height

    # функция, возвращающая баланс относительно принимаемой ноды
    def _get_balance(self, node: Node) -> int:
        if node is None:
            return 0
        else:
            return self._get_height(node.left) - self._get_height(node.right)

    # функция свапа значений двух узлов перед поворотом дерева при балансировке
    def _swap_nodes(self, first_node: Node, second_node: Node) -> None:
        first_value = first_node.value  # first_value выступает в роле буфера
        first_node.value = second_node.value
        second_node.value = first_value

    # правый поворот, при котором узел занимает место правого потомка
    # у своего левого потомка
    def _right_rotate(self, node: Node) -> None:
        # свапаем родителя и его левого потомка
        self._swap_nodes(node, node.left)
        # сохраняем правого потомка во временный буфер
        temp = node.right
        # на место правого потомка ставим левого
        node.right = node.left
        # на место левого потомка ставим левого у правого потомка
        node.left = node.right.left
        # на место левого у правого потомка ставим правого у правого потомка
        node.right.left = node.right.right
        # на место правого у правого потомка ставим правого потомка из буфера
        node.right.right = temp
        # обновляем высоту правого потомка
        self._update_height(node.right)
        # обновляем высоту самого узла
        self._update_height(node)

    # левый поворот, при котором узел занимает место левого потомка у своего
    # правого потомка
    def _left_rotate(self, node: Node) -> None:
        # свапаем родителя и его правого потомка
        self._swap_nodes(node, node.right)
        # сохраняем левого потомка во временный буфер
        temp = node.left
        # на место левого потомка ставим правого
        node.left = node.right
        # на место правого потомка ставим правого у левого потомка
        node.right = node.left.right
        # на место левого у правого потомка ставим правого у правого потомка
        node.right.left = node.right.right
        # на место правого у левого потомка ставим левого у левого потомка
        node.left.right = node.left.left
        # на место левого у левого потомка ставим левого потомка из буфера
        node.left.left = temp
        # параллельно обновляем высоту левого потомка
        self._update_height(node.left)
        # параллельно обновляем высоту самого узла
        self._update_height(node)

    # функция балансировки дерева
    def _balance(self, node: Node):
        # получение баланса относительно узла
        balance = self._get_balance(node)
        # -2 значит, что дерево перегружено влево и нужен поворот вправо
        if balance == -2:
            # левый правый поворот на случай, если правый поворот не избавит
            # от перегрузки дерева
            if self._get_balance(node.left) == 1:  # если у левого потомка
                self._left_rotate(node.left)       # перегрузка (0 - -1 = 1)
            self._right_rotate(node)
        # 2 значит, что дерево перегружено право и нужен поворот влево
        if balance == 2:
            # правый левый поворот на случай, если левый поворот не избавит
            # от перегрузки дерева
            if self._get_balance(node.right) == -1:  # если у правого потомка
                self._right_rotate(node.right)       # перегрузка (-1 - 0 = -1)
            self._left_rotate(node)

    '''
    Для трансформации дерева в строку используется метод __str__, вызывающий
    рекурсивную функцию _string и возвращающий элементы от меньшего к большему
    (согласно правилам возрастающего обхода бинарного дерева)
    Это позволит посмотреть, в правильной ли последовательности организованы
    все элементы
    '''

    def __str__(self):  # функция начинает с корня root
        return self._string(self.root)

    def _string(self, node: Node) -> str:  # функция применяется к каждому узлу
        if node is None:  # дерева и возвращает пустую строку
            return ''  # если такого узла нет (None)
        return (
            f"{self._string(node.left)}"  # каждый левый потомок каждой ноды
            f"{str(node.value)} "  # значение ноды
            f"{self._string(node.right)}")  # каждый правый потомок
        # результат переводится в строку, иначе выпадет ошибка
