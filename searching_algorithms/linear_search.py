import random
import time

'''
Complexity:
    Best = O(1)
    Average = O(n)
    Worst = O(n)
Compatibility with negative numbers: Yes
Speed: ~ 0.001s for 1_000_000++-sized list
'''


def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


array_linear_search = [
    random.randint(-10_000, 10_000) for _ in range(1_000_000)
]
start = time.time()
print(linear_search(array_linear_search, 1))
print(time.time() - start)