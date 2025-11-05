import math

n = 1

biblioteka = []

for i in range(n):
    print("Podaj wartość a, b i c (cyfry wpisuj oddzielone spacją):")
    dane = input()
    dane_split = dane.split()

    a = int(dane_split[0])
    b = int(dane_split[1])
    c = int(dane_split[2])

    biblioteka.append((a, b, c))

   
    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            print("Równanie ma dwa rozwiązania.")
        elif delta == 0:
            print("Równanie ma jedno rozwiązanie.")
        else:
            print("Równanie nie ma rozwiązań.")
    else:
        if b != 0:
            print("Równanie ma jedno rozwiązanie.")
        else:
            if c == 0:
                print("Równanie ma nieskończenie wiele rozwiązań.")
            else:
                print("Równanie sprzeczne, brak rozwiązań.")
