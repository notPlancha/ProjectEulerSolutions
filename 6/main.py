a = 0
b = 0
for i in range(1,101):
    a += i**2
    b += i
b **= 2
print(b-a)