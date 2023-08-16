
def radix_sort(arr):
    # Находим максимальное число и определяем количество разрядов
    max_num = max(arr)
    max_digits = len(str(max_num))

    # Создаем 10 пустых корзин
    buckets = [[] for _ in range(10)]

    # Проходимся по разрядам
    for digit in range(max_digits):
        # Распределяем элементы по корзинам
        for num in arr:
            # Получаем цифру разряда
            current_digit = (num // (10**digit)) % 10
            # Помещаем элемент в соответствующую корзину
            buckets[current_digit].append(num)

        # Собираем элементы из корзин в исходный массив
        arr = [num for bucket in buckets for num in bucket]
        # Очищаем корзины
        buckets = [[] for _ in range(10)]

    return arr


# Пример использования
nums = [329, 457, 657, 839, 436, 720, 355]
sorted_nums = radix_sort(nums)
print(sorted_nums)

