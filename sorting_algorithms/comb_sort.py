import random
import time

'''
Complexity:
    Best = O(n log(n))
    Average = O(n^2/2^p)
    Worst = O(n^2)
Compatibility with negative numbers: Yes
Speed: ~ 0.1s for 10_000-sized list
'''


def comb_sort(arr: list) -> list:
    gap = int(len(arr) // 1.247)
    swap = True
    while gap > 1 or swap:
        swap = False
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swap = True
            i += 1
        if gap > 1:
            gap = int(gap // 1.247)
    return arr


array_comb_sort = [
    random.randint(-10_000, 10_000) for _ in range(10_000)
]
start = time.time()
comb_sort(array_comb_sort)
print(time.time() - start)