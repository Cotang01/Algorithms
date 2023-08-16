import random
import time

'''
Complexity:
    Best = O(n log(n))
    Average = O(n log(n))
    Worst = O(n^2)
Compatibility with negative numbers: Yes
Speed: ~ 0.03s for 10_000-sized list
'''


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + middle + quick_sort(right)


array_quick_sort = [
    random.randint(-10_000, 10_000) for _ in range(10_000)
]
start = time.time()
print(quick_sort(array_quick_sort))
print(time.time() - start)
