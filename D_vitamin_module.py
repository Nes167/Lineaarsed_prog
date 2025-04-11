from random import *

def sisesta_andmed ():
    """Добавляем пациентов в список
    """
    nimed=[]
    D_vitamiini_sisaldus=[]
    try:
        n=int(input("Kui palju patsiente analüüsida? ")).isalpha()
        for i in range(n):
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
            d_vitamiin=random(10,100)
            D_vitamiini_sisaldus.append(d_vit)
    except: 
        print("Sisesta ainult tähed")
    return nimed, d_vitamiin

def puudus_vitamiin_d(nimed, d_vitamiin):
    print("\nD-vitamiini vaegusega patsiendid (alla 30):")
    for nimi, d_sisaldus in zip(nimed, d_vitamiin):
        if d_sisaldus < 30:
            print(f"{nimi}: {d_sisaldus} mcg/l")

def keskmine_vitamiin_d(d_vitamiin):
    average_vitamiin = sum(d_vitamiin) / len(d_vitamiin)
    print(f"\nKeskmine D-vitamiini tase: {average_vitamiin} mcg/l")

