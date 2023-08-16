import random
import time

'''
Complexity:
    Best = O(nk)
    Average = O(nk)
    Worst = O(nk)
Compatibility with negative numbers: No
Speed: ~ 0.01s for 10_000-sized list
'''


def radix_sort(arr):
    max_num = max(arr)
    max_digits = len(str(max_num))
    buckets = [[] for _ in range(10)]
    for digit in range(max_digits):
        for num in arr:
            current_digit = (num // (10**digit)) % 10
            buckets[current_digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
        buckets = [[] for _ in range(10)]
    return arr


array_radix_sort = [
    random.randint(0, 10_000) for _ in range(10_000)
]
start = time.time()
print(radix_sort(array_radix_sort))
print(time.time() - start)

