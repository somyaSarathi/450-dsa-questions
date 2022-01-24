import math
import time


def findDuplicate(nums: list[int], n: int) -> int:
    numSet = set()
    for num in nums:
        if num in numSet:
            return num
        numSet.add(num)

    return -1


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input())
    arr = [ int(x) for x in input().rstrip().split() ]

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)