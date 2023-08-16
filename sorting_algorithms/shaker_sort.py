import random
import time

''' SOMEHOW DOESN'T WORK
Complexity: -
Compatibility with negative numbers: -
Speed: -
'''


def shaker_sort(arr: list) -> list:
    left = 0
    right = len(arr) - 1
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
        return arr


array_shaker_sort = [
    random.randint(-10_000, 10_000) for _ in range(1_000)
]
print(array_shaker_sort)
start = time.time()
print(shaker_sort(array_shaker_sort))
print(time.time() - start)
