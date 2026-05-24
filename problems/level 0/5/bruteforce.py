ciclo = True
n = 0
while ciclo:
    n += 20
    print(n, end="\r")
    if n % 19 == 0 and n%18 == 0 and n % 17 == 0 and n % 16 == 0 and n % 15 == 0 and n % 14 == 0 and n % 13 == 0 and n % 12 == 0 and n%11 == 0:
        ciclo = False
print(n)