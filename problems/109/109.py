Scores = []
Doubles = []
count = 0
for i in range(1, 21):
    Scores.append(i)
    Scores.append(i*2)
    Doubles.append(i*2)
    Scores.append(i*3)
Scores.append(25)
Scores.append(50)
Doubles.append(50)
#miss miss double
count = len(Doubles)
#miss hit double
for d in Doubles:
    for s in Scores:
        if d+s < 100:
            count+= 1
#hit hit double
for d in Doubles:
    for s1 in range(len(Scores)):
        for s2 in range(s1, len(Scores)):
            if Scores[s1] + Scores[s2] + d < 100:
                count += 1
print(count)