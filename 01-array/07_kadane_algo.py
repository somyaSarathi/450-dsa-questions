import math
import time


def kadane(arr: list[int]) -> int:
    maxC = maxG = arr[0]
    for a in arr[1:]:
        maxC = max(a, maxC+a)
        maxG = max(maxG, maxC)
    return maxG


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input())
    arr = [ int(x) for x in input().split() ]

    # output
    print(kadane(arr))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)