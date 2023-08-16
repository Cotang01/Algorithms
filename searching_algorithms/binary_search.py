import random
import time

'''
Complexity:
    Best = O(log(n))
    Average = O(log(n))
    Worst = O(log(n))
Compatibility with negative numbers: Yes
Speed: ~ 0.001s for 1_000_000++-sized list
'''


def binary_search(arr: list, num: int) -> int:
    low = 0
    top = len(arr) - 1

    while low <= top:
        mid = (low + top) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            top = mid - 1
    return -1


array_binary_search = [
    random.randint(-10_000, 10_000) for _ in range(1_000_000)
]
start = time.time()
print(binary_search(array_binary_search, 1))
print(time.time() - start)