import math
import time


def union(a: list[int], b: list[int]) -> list[int]:
    setA = set(a)
    for e in b:
        setA.add(e)
    return len(setA)


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n, m = [ int(x) for x in input().split() ]
    a = [ int(x) for x in input().split() ]
    b = [ int(x) for x in input().split() ]

    # output
    print(union(a, b))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)