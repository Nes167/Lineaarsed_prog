from telefoniraamat_funktsioon import *
fail="telefoniraamat.txt"
telefoniraamat=loefailist(fail)

while True:
    print("Menu:")
    print("1 - Näita kõiki kontakte\n2 - Lisa uus kontakt\n3 - Otsi kontakti nime järgi\n4 - Kustuta kontakt\n5 - Muuda kontakt\n6 - Sorteeri kontakt\n7-Saada e-kiri kontaktile\n0 - Välja")
    valik = input("\nSisesta valik: ")
    if valik == "1":
        kuva_kontaktid(telefoniraamat)
    elif valik == "2":
         lisa_kontakt(telefoniraamat)
    elif valik == "3":
        otsi_kontakt(telefoniraamat)     
    elif valik == "4":
        kustuta_kontakt()    
    elif valik == "5":
        paranda_kontakt(telefoniraamat) 
    elif valik == "6":
        sorteeri_kontakt()
    elif valik == "7":
        saada_kiri()
    elif valik == "0":
        salvesta_sonad(fail,telefoniraamat)
        break
    else:
        print("Viga! Proovi veel kord.")
