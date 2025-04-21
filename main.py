from sonastik import *
print("Tere tulemast kolme keele sõnastikku!")
sonad = loo_sonastik()
while True:
    print("\nMenu:")
    print("1 - Tõlgi sõna\n2 - Lisa uus sõna \n3 - Paranda sõna\n4 - Kuva kõik sõnad\n5 - Testi teadmisi\n0 - Välja")
    valik = input("\nSisesta valik: ")
    if valik == "1":
        allikas, siht=vali_keelte_suund()
        sona=input(f"Sisesta sõna({allikas})")
        print(f"Tõlge: {tolkija(sonad,allikas, siht, sona)}")   
    elif valik == "2":
         lisa_sona(sonad)
    elif valik == "3":
        paranda_sona(sonad)     
    elif valik == "4":
        kuva_sonad(sonad)    
    elif valik == "5":
        testi_teadmisi(sonad)       
    elif valik == "0":
        break
    else:
        print("Viga! Proovi veel kord.")