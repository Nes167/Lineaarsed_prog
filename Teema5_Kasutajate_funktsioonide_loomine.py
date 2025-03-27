from Teema5_funktsioonide_kasutamine import *

#Ülesanne1
try:
    while True:
        if a!=float:
            a=float(input("Arv1: "))
        else:
            break
        while True:
            if b!=float:
                b=float(input("Arv2: "))
            else:
                break
            while True:
                if t!=str:
                    t=str(input("Tehe: "))
                else:
                    break
                    vastus=arithmetic(a,b,t)
                    print(vastus)

                    vastus=arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),float(input("Tehe: ")))
                    print(vastus)
except:
    print("Viga")


#Ülesanne2
aasta=int(input("Mis aasta tahad kontrollida? "))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigiaasta")
    else:
        print(f"{aasta} ei ole liigiaasta")


#Ülesanne 3
while True:
    try:
        a=float(input("Sisesta ruudu külg: "))
        if a>0 and a==float:
            break
        S,P,d=square(a)
        print(S,P,d)
    except:
        print("Viga")


#Ülesanne 4
while True:
    try:
        m=int(input("Sisesta kuu: "))
        break
    except:
        print("Viga!")
v=season(m)
print(v)

#Ülesanne 5
while True:
    try:
        summa=float(input("Sisesta summa: "))
        break
        while True:
            try:
                aastad=int("Sisesta aasta:")
                break
            except:
                print("Viga! Sisesta arv")
    except:
        print("Viga! Sisesta arv")
vastus=bank(summa)
print(vastus)

# Ülesanne 6
if is_prime():
    print("True")
else:
    print("False")

#Ülesanne 7
try:
    päev=int(input("Sisesta päev: "))
    kuu=int(input("Sisesta kuu: "))
    aasta=int(input("Sisesta aasta: "))
    v=date(päev,kuu,aasta)
    print(v)
except:
    print("viga!")







