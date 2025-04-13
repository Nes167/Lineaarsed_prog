from D_vitamin_module import *

nimed, d_vitamiin = sisesta_andmed() # Заполнение данных

while True:
    print("\nAndmed:")
    loend = zip(nimed, d_vitamiin)  # Объединяем имена и уровни витамина
    for nimi, d_tase in loend:  # Проходимся по каждому пациенту
        print(f"{nimi}: {d_tase} mcg/l")
    print("\nMenu:")
    print("1 - D-vitamiini vaegusega patsiendid (alla 30)\n2 - Leia ja kuva keskmine D-vitamiini tase\n3 - Näita K patsienti kõige kõrgema D-vitamiini tasemega\n4 - Otsi patsiendi nime järgi ja kuva tema D-vitamiini tase\n5 - Kuva patsiendid, kelle D-vitamiini tase on alla keskmise\n0 - Välja")
    valik = input("\nSisesta valik: ")
    if valik == "1":
        puudus_vitamiin_d(nimed, d_vitamiin)
    elif valik == "2":
        keskmine_vitamiin_d(d_vitamiin)
    elif valik == "3":
        top_k_vitamiin_d(nimed, d_vitamiin)
    elif valik == "4":
        otsi_patsiendi_vitamiin_d(nimed, d_vitamiin)
    elif valik == "5":
        alla_keskmise(nimed, d_vitamiin)
    elif valik == "0":
        break
    else:
        print("Viga! Proovi veel kord.")
