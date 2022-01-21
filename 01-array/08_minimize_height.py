import math
import time


# considering arr in sorted
def getMinDiff(arr: list[int], k: int) -> int:
    arr.sort()
    res = arr[-1]-arr[0]
    
    for i in range(1, n):
        if arr[i] >= k:
            mx = max(arr[i-1]+k, arr[-1]-k)
            mn = min(arr[i]-k, arr[0]+k)
            res = min(mx-mn, res)
            
    return res


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n, k = [ int(x) for x in input().split() ]
    arr = [ int(x) for x in input().split() ]

    # output
    print(getMinDiff(arr, k))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)