s = 0
lista = input("Podaj liczby")
for i in lista:
    if i != " ":
        s += float(i)
print(s)