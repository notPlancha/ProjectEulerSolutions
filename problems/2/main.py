endFib = False
def fib():
    ult = 2
    current = 3
    while not endFib:
        #starts from third term
        yield current
        pen = ult
        ult = current
        current = ult + pen

if __name__ == '__main__':
    currFibNumb = 1
    gen = fib()
    sum = 0
    while currFibNumb < 4000000:

        if currFibNumb % 2 == 1:
            sum += currFibNumb
        currFibNumb = next(gen)
    print(sum + 1)