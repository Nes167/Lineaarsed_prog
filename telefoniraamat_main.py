from telefoniraamat_funktsioon import *
fail="telefoniraamat.txt"
telefoniraamat=loefailist(fail)

while True:
    print("Menu:")
    print("1 - Näita kõiki kontakte\n2 - Lisa uus kontakt\n3 - Otsi kontakti nime järgi\n4 - Kustuta kontakt\n5 - Muuda kontakt\n6 - Sorteeri kontakt\n7 - Saada e-kiri kontaktile\n0 - Välja")
    valik = input("\nSisesta valik: ")
    if valik == "1":
        kuva_kontaktid(telefoniraamat)
    elif valik == "2":
         lisa_kontakt(telefoniraamat)
    elif valik == "3":
        otsi_kontakt(telefoniraamat)     
    elif valik == "4":
        kustuta_kontakt(telefoniraamat)    
    elif valik == "5":
        paranda_kontakt(telefoniraamat) 
    elif valik == "6":
        sorteeri_kontakt(telefoniraamat)
    elif valik == "7":
        saada_kiri()
    elif valik == "0":
        Kirjutafailisse(fail,telefoniraamat)
        break
    else:
        print("Viga! Proovi veel kord.")

# from tkinter import *
# from tkinter import messagebox

# aken=Tk()
# aken.title("Telefoniraamat")
# aken.geometry("900x600")
# aken.configure(bg="lightblue")
# aken.resizable(width=False, height=False)
# aken.iconbitmap("phonebook.ico")
# pealkiri=Label(aken,text="Telefooniraamat",bg="blue",fg="white",font=("Arial",20))
# nupp1=Button(aken,text="Kuva kontaktid",bg="red",fg="white",font=("Arial",15))
# nupp1.bind('<Button-1>',kuva_kontaktid)
# nupp2=Button(aken,text="Lisa kontakt",bg="red",fg="white",font=("Arial",15))
# nupp2.bind('<Button-1>',lisa_kontakt)
# nupp3=Button(aken,text="Otsi kontakt",bg="red",fg="white",font=("Arial",15))
# nupp3.bind('<Button-1>',otsi_kontakt)
# nupp4=Button(aken,text="Kustuta kontakt",bg="red",fg="white",font=("Arial",15))
# nupp4.bind('<Button-1>',kustuta_kontakt)
# nupp5=Button(aken,text="Paranda kontakt",bg="red",fg="white",font=("Arial",15))
# nupp5.bind('<Button-1>',paranda_kontakt)
# nupp6=Button(aken,text="Sorteeri kontakt",bg="red",fg="white",font=("Arial",15))
# nupp6.bind('<Button-1>',sorteeri_kontakt)
# nupp7=Button(aken,text="Saada kiri",bg="red",fg="white",font=("Arial",15))
# nupp7.bind('<Button-1>',saada_kiri)
# nupp8=Button(aken,text="Välju",bg="red",fg="white",font=("Arial",15))
# nupp8.bind('<Button-1>',Kirjutafailisse)

# pealkiri.pack(pady=10)
# nupp1.pack(pady=10)
# nupp2.pack(pady=10)
# nupp3.pack(pady=10)
# nupp4.pack(pady=10)
# nupp5.pack(pady=10)
# nupp6.pack(pady=10)
# nupp7.pack(pady=10)
# nupp8.pack(pady=10)
# aken.mainloop()
