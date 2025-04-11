from D_vitamin import *

nimed=[]
D_vitamiini_sisaldus=[] 
def patsiendid():
    nimed,d_vitamiin=sisesta_andmed()

while True:
    print("Andmed: ")
    print(nimed)
    print(D_vitamiini_sisaldus)
    print("Menu:")
    print("1-Leia keskmine D-vitamiini tase\n2-Kuvage K kõrgeima punktisumma saanud inimese nimekiri\n3-Otsige töötajaid nime järgi ja kuvage tulemused ekraanile\n4-oma variant")
    valik=int(input())
    if valik == "1":
            puudus_vitamiin_d(nimed, d_vitamiin)
    elif valik == "2":
        keskmine_vitamiin_d(d_vitamiin)
