from tqdm import tqdm
from math import sqrt

phy = (1+sqrt(5))/2
from tqdm import tqdm

def fib(n):
    if n in [1, 2]:
        return 1
    current = 1
    for i in range(3, n + 1):
        current *= phy
    return current


def continuousFib(untilCondition):
    current = 1
    n = 3
    while not untilCondition(current):
        print(n, end="\r")
        current *= phy
        n += 1
    return n-1

def firstAndLastPan(v):
    s = str(v)
    return set('123456789') == set(s[:9]) and set('123456789') == set(s[-9:])

def isPandigital(s):
    return set(s) == set('123456789')

if __name__ == '__main__':
    print("Running")
    print(continuousFib(firstAndLastPan))