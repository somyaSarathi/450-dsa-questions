import math
import time


def mergeArray(a: list[int], b: list[int], n: int, m: int) -> None:
    i = n-1
    j = 0
    while i>=0 and j<m:
        if a[i] > b[j]:
            a[i], b[j] == b[j], a[i]
        i -= 1
        j += 1

    a.sort()
    b.sort()

    return None


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n, m = [ int(x) for x in input().rstrip().split() ]
    a = [ int(x) for x in input().rstrip().split() ]
    b = [ int(x) for x in input().rstrip().split() ]
    mergeArray(a, b, n, m)

    print(a)
    print(b)

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)