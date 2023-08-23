# инициализация класса узел
class Node:
    def __init__(self, value=None, colour=1):
        self.value = value  # значение
        self.left = None  # левый потомок
        self.right = None  # правый потомок
        self.colour = colour  # 0 - чёрный, 1 - красный

    # перевод узла в строку
    def __str__(self):
        return f'{self.value, self.colour, self.left, self.right}'

    '''
    Красно-черное дерево имеет следующие критерии:
    • Каждая нода имеет цвет (красный или черный)
    • Корень дерева всегда черный
    • Новая нода всегда красная
    • Красные ноды могут быть только левым ребенком
    • У красной ноды все дети черного цвета
    '''


class RedBlackTree:
    # при инициализации создаётся root, который будет являться корнем дерева
    def __init__(self):
        self.root = None

    # метод поиска элемента по значению
    def find(self, value: int) -> Node:
        return self._find_assist(self.root, value)

    '''
    Вспомогательная функция поиска элемента по значению нужна, чтобы 
    поиск был возможен при условии принятия только значения искомого элемента
    то есть чтобы не требовалось дополнительных данных для получения результата
    '''

    # вспомогательная рекурсивная функция
    def _find_assist(self, current: Node, value: int) -> Node:
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
    значение, а затем уже сама добавляла узел там, где это нужно исходя из 
    критериев дерева (меньшие значения слева, большие - справа)
    В одной функции не удаётся удовлетворить все требования из-за особенности
    рекурсии, поэтому она делится на 2 функции, 1 из которых рекурсивна
    
    Параллельно при скрутке стека рекурсии балансируем дерево на основе
    заложенных в балансировку условий
    '''

    # метод вставки узла по значению
    def insert(self, value: int) -> bool:
        if self.root is not None:
            result = self._insert_assist(self.root, value)
            self.root = self._balance(self.root)
            self.root.colour = 0
            return result
        else:
            self.root = Node(value)
            self.root.colour = 0
            return True

    # вспомогательная рекурсивная функция вставки узла
    def _insert_assist(self, node: Node, value: int) -> bool:
        if node.value > value:  # если добавляемое значение меньше узла
            if node.left is not None:  # и если место занято, то ищем место
                result = self._insert_assist(node.left, value)
                node.left = self._balance(node.left)
                return result
            else:  # если место не занято, то инициализируем узел с нашим
                node.left = Node(value)  # значением и добавляем его
                return True
        if node.value < value:  # если добавляемое значение больше узла
            if node.right is not None:  # и если место занято, то ищем место
                result = self._insert_assist(node.right, value)
                node.right = self._balance(node.right)  # балансировка
                return result
            else:  # если место не занято, то инициализируем узел с нашим
                node.right = Node(value)  # значением и добавляем его
                return True
        else:  # если не удалось найти место, то возвращаем False
            return False

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

    # функция удаления узла по значению
    def delete(self, value: int) -> None:
        if self.root.value == value:
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                node_max_left = self._min_find(self.root.right)
                self.root.value = node_max_left.value
                self.root.right = self._delete_assist(self.root.right,
                                                      node_max_left.value)
        else:
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
                максимальный элемент слева от узла, который встанет на его
                место.
                Передаём значение.
                Рекурсивно удаляем элемент, от которого перенималось значение.
                """
                node_max_left = self._min_find(del_node.right)
                del_node.value = node_max_left.value
                del_node.right = self._delete_assist(del_node.right,
                                                     node_max_left.value)
        return del_node

    # функция поиска минимального значения
    def _min_find(self, node: Node) -> Node:
        if node is None:
            return None
        if node.left is None:
            return node
        return self._min_find(node.left)

    # функция поиска максимального значения
    def _max_find(self, node: Node) -> Node:
        if node is None:
            return None
        if node.right is None:
            return node
        return self._max_find(node.right)

    '''
    Балансировка дерева.
    Для того, чтобы наше дерево было сбалансированным (чтобы сложность 
    поиска, вставки и удаления всегда была O(log(n))), надо при каждом добавлении 
    элемента обрабатывать несколько возникаемых ситуаций.
    
    Балансировка будет происходить до тех пор, пока все 3 условия не будут 
    удовлетворены.
    '''

    def _balance(self, node: Node) -> Node:
        result = node
        need_balance = True
        while need_balance:
            need_balance = False
            """
            если правый потомок существует, его цвет - красный и либо
            отсутствует левый потомок, либо цвет левого потомка - чёрный, то
            производится правый поворот и следующие действия для балансировки
            """
            if result.right is not None and result.right.colour == 1 and \
                    (result.left is None or result.left.colour == 0):
                need_balance = True
                result = self._right_rotate(result)
            """
            если левый потомок существует и его цвет - красный и левый
            потомок левого потомка существует и его цвет тоже красный, то
            производится левый поворот и следующие действия для балансировки
            """
            if result.left is not None and \
                    result.left.colour == 1 and \
                    result.left.left is not None and \
                    result.left.left.colour == 1:
                need_balance = True
                result = self._left_rotate(result)
            """
            если левый потомок существует и его цвет - красный и правый 
            потомок также существует и его цвет тоже красный, 
            то производится смена цвета, при которой родитель становится 
            красным, а его потомки - чёрными
            """
            if result.left is not None and result.left.colour == 1 and \
                    result.right is not None and result.right.colour == 1:
                need_balance = True
                self._colour_swap(result)
        return result

    # изменение цвета
    @staticmethod
    def _colour_swap(node: Node) -> None:
        node.left.colour = 0  # левый потомок становится чёрным
        node.right.colout = 0  # правый потомок становится чёрным
        node.colour = 1  # родитель становится красным

    # правый поворот
    @staticmethod
    def _right_rotate(node: Node) -> Node:
        right = node.right  # сохраняем правого потомка в буфер
        between = right.left  # в качестве промежуточного потомка выступает
        # левый потомок
        right.left = node  # меняем местами родителя и его левого потомка
        node.right = between  # на место правого потомка ставим промежуточного
        right.colour = node.colour  # правый потомок перенимает цвет родителя
        node.colour = 1  # родитель становится красным
        return right

    # левый поворот
    @staticmethod
    def _left_rotate(node: Node) -> Node:
        left = node.left  # сохраняем левого потомка в буфер
        between = left.right  # в качестве промежуточного потомка выступает
        # правый потомок
        left.right = node  # меняем местами родителя и его правого потомка
        node.left = between  # на место левого потомка ставим промежуточного
        left.colour = node.colour  # левый потомок перенимает цвет родителя
        node.colour = 1  # родитель становится красным
        return left

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
            f'{self._string(node.left)}'  # каждый левый потомок каждой ноды
            f'{str(node.value)} '  # значение ноды
            f'{self._string(node.right)}')  # каждый правый потомок
        # результат переводится в строку, иначе выпадет ошибка
