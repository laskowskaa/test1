lista = list()
pierwszy = input()
lista.append(pierwszy)
drugi  = input()
lista.append(drugi)
trzeci = input()
lista.append(trzeci)
czwarty  = input()
lista.append(czwarty)
piaty  = input()
lista.append(piaty)
licznik = 0
for el in lista:
    if el[0].isupper():
        licznik = licznik + 1
print(licznik)