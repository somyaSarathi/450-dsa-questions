import math
import time


def kMinMax(arr: list[int], N: int, K: int):
    arr.sort()
    return arr[K-1]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    N, K = [ int(x) for x in input().split() ]
    arr = [ int(x) for x in input().split() ]

    # output
    print(f'{K} smallest element {kMinMax(arr, N, K)}')

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)