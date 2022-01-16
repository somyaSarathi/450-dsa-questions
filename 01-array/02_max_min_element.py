import math
import time


def maxMin(arr: list[int]):
    mx = max(arr)
    mn = min(arr)
    return mx, mn


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input())
    arr = [ int(x) for x in input().split() ]

    # output
    mx, mn = maxMin(arr)
    print(f'max is {mx}')
    print(f'min is {mn}')

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)