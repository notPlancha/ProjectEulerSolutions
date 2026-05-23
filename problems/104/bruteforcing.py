from tqdm import tqdm

def fib(n):
    if n in [1, 2]:
        return 1
    ult = pen = current = 1
    for i in range(3, n + 1):
        current = pen + ult
        pen = ult
        ult = current
    return current


def continuousFib(untilCondition):
    ult = pen = current = 1
    n = 3
    while not untilCondition(current):
        print(n, end="\r")
        current = pen + ult
        pen = ult
        ult = current
        n += 1
    return n-1

def firstAndLastPan(v):
    s = str(v)
    return isPandigital(s[:9]) and isPandigital(s[-9:])

def isPandigital(s):
    return set(s) == set('123456789')

if __name__ == '__main__':
    print(continuousFib(firstAndLastPan))