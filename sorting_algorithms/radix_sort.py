import random
import time


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
    random.randint(-10_000, 10_000) for _ in range(10_000)
]
start = time.time()
radix_sort(array_radix_sort)
print(time.time() - start)

