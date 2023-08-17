import random
import time

'''
Complexity:
    Best = O(n log(n))
    Average = O(n log(n))
    Worst = O(n log(n))
Compatibility with negative numbers: Yes
Speed: ~ 0.04s for 10_000-sized list
'''


def heapify(arr: list, n: int, i: int):  # список, длина списка, узел
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if right < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


array_heap_sort = [
    random.randint(-10_000, 10_000) for _ in range(10_000)
]
start = time.time()
heap_sort(array_heap_sort)
print(time.time() - start)
