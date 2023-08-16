import random
import time

'''
Complexity:
    Best = O(n)
    Average = O(n^2)
    Worst = O(n^2)
Compatibility with negative numbers: Yes
Speed: ~ 5.8s for 10_000-sized list
'''


def bubble_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array_bubble_sort = [
    random.randint(-10_000, 10_000) for _ in range(10_000)
]
start = time.time()
bubble_sort(array_bubble_sort)
print(time.time() - start)
