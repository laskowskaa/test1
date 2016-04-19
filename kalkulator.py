lista1 = list()
pierwszy = input()
lista1.append(pierwszy)
drugi  = input()
lista1.append(drugi)
trzeci = input()
lista1.append(trzeci)
czwarty  = input()
lista1.append(czwarty)
piaty  = input()
lista1.append(piaty)
licznik = 0
for el in lista1:
    if el[0].isupper():
        licznik = licznik + 1
print(licznik)
def mnozenie(x,y):
    return(x*y)