from math import *
print("Ruudu karakteristikud")
try:
    a=int(input('Sisesta ruudu külje pikkus => '))
    if a>0:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P)
        di=a*sqrt(2)
        print("Ruudu diagonaal", round(di,2))
    else:
        print("külg ei saa olla 0 või vähem.")
except:
    print("Viga! sisesta ainult täisarvud!")
    

print("Ristküliku karakteristikud")
try:
    b=int(input("Sisesta ristküliku 1. külje pikkus => "))
    c=int(input("Sisesta ristküliku 2. külje pikkus => "))
    if b>0 and c>0:
        S=b*c
        print("Ristküliku pindala", S)
        P=2*(b+c)
        print("Ristküliku ümbermõõt", P)
        di=sqrt(b*2+c*2)
        print("Ristküliku diagonaal", round(di))
    else:
        print("b ja c ei saa olla 0 või vähem.")
except:
    print("Viga! sisesta ainult täisarvud!")


print("Ringi karakteristikud")
try:
    r=int(input("Sisesta ringi raadiusi pikkus => "))
    if r>0:
        d=2*r
        print("Ringi läbimõõt", d)
        S=pi*r**2
        print("Ringi pindala", round(S))
        C=2*pi*r
        print("Ringjoone pikkus", round(C))
    else:
        print("r ei saa olla 0 või vähem.")
except:
    print("Viga! sisesta ainult täisarvud!")

