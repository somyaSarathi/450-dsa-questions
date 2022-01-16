import math
import time


def reverse(arr: list[int]) -> list[int]:
    return arr[:][::-1]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n: int = int(input())
    arr: list[int] = [ int(x) for x in input().split() ]

    # output
    arr = reverse(arr)
    for a in arr:
        print(a, end=' ')
    print('\n')

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)