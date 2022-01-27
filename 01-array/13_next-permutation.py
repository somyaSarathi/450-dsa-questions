import math
import time


def nextPermutation(nums: list[int]) -> None:
    i = len(nums)-2
    while i>=0 and nums[i] >= nums[i+1]:
        i -= 1
    if i>=0:
        j = len(nums)-1
        while(nums[j]<=nums[i]):
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    reverse(nums, i+1)


def reverse(arr: list[int], start: int) -> None:
    j = len(arr)-1
    while(start < j):
        nums[start], nums[j] = nums[j], nums[start]
        start += 1
        j -= 1

if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input())
    nums = [ int(x) for x in input().rstrip().split() ]
    nextPermutation(nums)
    print(nums)

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)