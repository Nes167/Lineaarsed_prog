import tkinter as tk
from tkinter import messagebox
from tel_funktsioon2 import *




kontaktid = loe_failist()

def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt_gui():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        lisa_kontakt(kontaktid, nimi,telefon,email)
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Edu","kontakt lisatud.")
        nimi_entry.delete(0,'end')
        telefon_entry.delete(0,'end')
        email_entry.delete(0,'end')
        kuva_kontaktid()
    else:
        messagebox.showwarning("Tühjad väljad","Täida kõik väljad")

def otsi_kontakt_gui():
    nimi = nimi_entry.get
    tulemused=otsi_kontakt(kontaktid, nimi)
    if tulemused:
        kontakt=tulemused[0]
        otsingu_viide.set(kontakt["nimi"])
        nimi_entry.delete(0,'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0,'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0,'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0",'end')
        tekstikast.insert("end", "Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")

def kustuta_kontakt_gui():
    nimi = nimi_entry.get()
    if kustuta_kontakt(kontaktid, nimi):
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Kustutatud", f"'{nimi}' kustutati.")
        kuva_kontaktid()
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")

def sorteeri_gui():
    kontaktid_sorted=sorteeri_kontaktid(kontaktid, "nimi")
    tekstikast.delete("1.0","end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")


# def muuda_kontakt_gui():
#     nimi = simpledialog.askstring("Muuda", "Sisesta nimi, keda muuta:")
#     for k in telefoniraamat:
#         if nimi.lower() in k['nimi'].lower():
#             uus_nimi = simpledialog.askstring("Uus nimi", "Sisesta uus nimi:", initialvalue=k['nimi'])
#             uus_email = simpledialog.askstring("Uus email", "Sisesta uus e-mail:", initialvalue=k['email'])
#             uus_telefon = simpledialog.askstring("Uus telefon", "Sisesta uus telefon:", initialvalue=k['telefon'])
#             if uus_nimi and uus_email and uus_telefon:
#                 k['nimi'] = uus_nimi
#                 k['email'] = uus_email
#                 k['telefon'] = uus_telefon
#                 naita_kontakte()
#                 messagebox.showinfo("Muudetud", "Kontakt on muudetud.")
#                 return
#     messagebox.showwarning("Ei leitud", "Kontakt puudub.")




aken = tk.Tk()
aken.title("Telefoniraamat")
aken.iconbitmap("phonebook.ico")
aken.configure(bg="pink")
otsingu_viide=tk.StringVar() #IntVar() #Muudame StringVar-iks, et saaksime salvestada algse nime
otsingu_viide.set("")
tk.Label(aken, text="Nimi: ",font=("Rockwell",10),fg="black").pack()
nimi_entry=tk.Entry(aken)
nimi_entry.pack()
tk.Label(aken, text="E-mail: ",font=("Rockwell",10),fg="black").pack()
email_entry=tk.Entry(aken)
email_entry.pack()
tk.Label(aken, text="Telefon: ",font=("Rockwell",10),fg="black").pack()
telefon_entry=tk.Entry(aken)
telefon_entry.pack()

nupude_rida=tk.Frame(aken)
nupude_rida.pack(pady=5)



tk.Button(nupude_rida, text="Kuva kontaktid", command=kuva_kontaktid,font=("Rockwell",12),fg="black").pack(side="left",pady=2)
tk.Button(nupude_rida, text="Lisa kontakt", command=lisa_kontakt_gui,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Otsi kontakt", command=otsi_kontakt_gui,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Kustuta kontakt", command=kustuta_kontakt_gui,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Sorteeri kontakt", command=sorteeri_gui,font=("Rockwell",12),fg="black").pack(side="left")
# tk.Button(nupude_rida, text="Muuda kontakt", command=muuda_kontakt_gui,font=("Rockwell",12),fg="black").pack(side="left")




tekstikast = tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)




aken.mainloop()
