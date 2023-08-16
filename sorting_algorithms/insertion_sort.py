import random
import time

'''
Complexity:
    Best = O(n)
    Average = O(n^2)
    Worst = O(n^2)
Compatibility with negative numbers: Yes
Speed: ~ 2.5s for 10_000-sized list
'''


def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


array_insertion_sort = [
    random.randint(-10_000, 10_000) for _ in range(10_000)
]
start = time.time()
insertion_sort(array_insertion_sort)
print(time.time() - start)
