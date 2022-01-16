import math
import time


def rotate(arr: list[int]) -> list[int]:
    return arr[-1:]+arr[:-1]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input())
    arr = [ int(x) for x in input().split() ]

    # output
    result = rotate(arr)
    for a in result:
        print(a, end=' ')
    print('\n')

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)