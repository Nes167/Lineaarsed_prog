from Teema5_funktsioonide_kasutamine import *

# #Ülesanne1
# a=float(input("Arv1: "))
# b=float(input("Arv2: "))
# t=str(input("Tehe: "))
# vastus=arithmetic(a,b,t)
# print(vastus)

# vastus=arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),float(input("Tehe: ")))
# print(vastus)

#Ülesanne2
aasta=int(input("Mis aasta tahad kontrollida? "))
if aasta<0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigiaasta")
    else:
        print(f"{aasta} ei ole liigiaasta")
