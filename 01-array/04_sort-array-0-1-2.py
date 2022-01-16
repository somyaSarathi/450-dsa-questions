import math
import time


def sort012(arr: list[int]) -> list[int]:
    count = {0:0, 1:0, 2:0}
    for a in arr:
        count[a] += 1
    return [0]*count[0]+[1]*count[1]+[2]*count[2]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input())
    arr = [ int(x) for x in input().split() ]

    # output
    result = sort012(arr)
    for ele in result:
        print(ele, end=' ')
    print('\n')

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)