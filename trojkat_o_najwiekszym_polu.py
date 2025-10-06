import math 

print("Podaj liczbę trójkątów")
n = int(input())

trojkaty = []

najwieksze_pole = 0

for i in range(n):
    print(f"Podaj długości boków trójkąta nr { i + 1 } (liczby nuszą być oddzielone spacją):")
    dane = input()
    dane_split = dane.split()
    a = int(dane_split[0])
    b = int(dane_split[1])
    c = int(dane_split[2])
    trojkaty.append((a, b, c))


    if a + b > c and a + c > b and b + c > a:
        p = ( a + b + c ) / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

        if pole > najwieksze_pole:
            najwieksze_pole = pole

    else: 
        print("Z podanych boków nie da się zbudować trójkąta.")


print(f"Największe pole trójkąta to: {najwieksze_pole:.2f}" )
