a = True
while a:
    n1 = input("Podaj liczbe1")
    n2 = input("Podaj liczbe2")
    i = input("Podaj operacje, e - zakoncz")
    if i is "+":
        print(int(n1) + int(n2))
    if i is "-":
        print(int(n1) - int(n2))
    if i is "*":
        print(int(n1) * int(n2))
    if i is "/" and n2 is not 0:
        print(int(n1) / int(n2))
    if i is "e":
        a = False
