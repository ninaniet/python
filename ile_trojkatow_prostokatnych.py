

print("Wpisz ilość elementów:")
n = int(input())

biblioteka=[]

for i in range(n):
    print(f"Podaj liczbę nr {i + 1} :")
    x = int(input())
    biblioteka.append(x)

ile_trojkatow = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = biblioteka[i]
            b = biblioteka[j]
            c = biblioteka[k]


            boki = sorted([a, b, c])

            if boki[0]**2 + boki[1]**2 == boki[2]**2:
                ile_trojkatow += 1


print("Liczba trójkątów prostokątnych: " + str(ile_trojkatow))