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
    nimi = nimi_entry.get()
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
        tekstikast.insert("end", f"Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
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

def sorteeri_tagurpidi_gui():
    kontaktid_sorted = sorteeri_tagurpidi(kontaktid, "nimi")
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")


def muuda_kontakt_gui():
    vana_nimi = otsingu_viide.get()
    uus_nimi = nimi_entry.get()
    uus_telefon = telefon_entry.get()
    uus_email = email_entry.get()
    if vana_nimi and uus_email and uus_telefon and uus_email:
        õnnestus=muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email)
        if õnnestus:
            salvesta_kontaktid(kontaktid)
            messagebox.showinfo("Muudetud", f"'{vana_nimi}' andmed on muudetud.")
            kuva_kontaktid()
        else:
            messagebox.showwarning("Tõrge", "Kontakti ei leitud muudatuseks.")
    else:
       messagebox.showwarning("Puuduvad andmed", "Palun täida kõik väljad.")

def kuva_kontaktide_arv():
    arv = kontaktide_arv(kontaktid)
    messagebox.showinfo("Kontaktide arv", f"Kontaktide koguarv: {arv}")

def puhasta_valjad():
    nimi_entry.delete(0, 'end')
    telefon_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    tekstikast.delete("1.0", "end")

def kuva_emailid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['email']}\n")

def otsi_email_gui():
    email = email_entry.get()
    tulemused = otsi_emaili_jargi(kontaktid, email)
    tekstikast.delete("1.0", "end")
    if tulemused:
        for kontakt in tulemused:
            tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showwarning("Ei leitud", "E-maili järgi kontakti ei leitud.")

def saada_kiri_aken():
    kiri_aken=tk.Tk()
    kiri_aken.title("Saada kiri")
    tk.Label(kiri_aken, text="Kellele: ",font=("Haettenschweiler",12),fg="red",  bg="pink").pack()
    kellele_entry=tk.Entry(kiri_aken)
    kellele_entry.pack()
    tk.Label(kiri_aken, text="Kellelt: ",font=("Haettenschweiler",12),fg="red",  bg="pink").pack()
    kellelt_entry=tk.Entry(kiri_aken)
    kellelt_entry.pack()
    tk.Label(kiri_aken, text="Teema: ",font=("Haettenschweiler",12),fg="red",  bg="pink").pack()
    teema_entry=tk.Entry(kiri_aken)
    teema_entry.pack()
    tk.Label(kiri_aken, text="Kiri: ",font=("Haettenschweiler",12),fg="red",  bg="pink").pack()
    tekstikast1 = tk.Text(kiri_aken, height=10, width=50)
    tekstikast1.pack(pady=10)
    tk.Label(kiri_aken, text="Parool: ",font=("Haettenschweiler",12),fg="red",  bg="pink").pack()
    parool_entry=tk.Entry(kiri_aken)
    parool_entry.pack()

    nupude_rida3=tk.Frame(kiri_aken)
    nupude_rida3.pack(pady=5)
    tk.Button(nupude_rida3, text="Saada", command=saada(kellele_entry,kellelt_entry,teema_entry, parool_entry,tekstikast1,kiri_aken),font=("Haettenschweiler",14),fg="black", bg="pink").pack(side="right",pady=0)
    
def saada(kellele_entry,kellelt_entry,teema_entry, parool_entry,tekstikast1,kiri_aken):
    kellele = kellele_entry.get()
    kellelt = kellelt_entry.get()
    teema = teema_entry.get()
    kiri = tekstikast1.get("1.0","end")
    parool = parool_entry.get()
    if kellele and kellelt and teema and parool and kiri:
        õnnestus=saada_kiri(kellele, kellelt, teema, parool, kiri)
        if õnnestus:
            messagebox.showinfo("Õnnestus","Kiri saadetud.")
            kiri_aken.destroy()
    else:
        messagebox.showwarning("Viga", "Kiri ei ole saadetud.")






aken = tk.Tk()
aken.title("Telefoniraamat")
aken.iconbitmap("phonebook.ico")
aken.configure(bg="pink")
otsingu_viide=tk.StringVar() #IntVar() #Muudame StringVar-iks, et saaksime salvestada algse nime
otsingu_viide.set("")
tk.Label(aken, text="Nimi: ",font=("Haettenschweiler",12),fg="red",  bg="pink").pack()
nimi_entry=tk.Entry(aken)
nimi_entry.pack()
tk.Label(aken, text="E-mail: ",font=("Haettenschweiler",12),fg="red", bg="pink").pack()
email_entry=tk.Entry(aken)
email_entry.pack()
tk.Label(aken, text="Telefon: ",font=("Haettenschweiler",12),fg="red", bg="pink").pack()
telefon_entry=tk.Entry(aken)
telefon_entry.pack()

nupude_rida=tk.Frame(aken)
nupude_rida.pack(pady=5)

nupude_rida1=tk.Frame(aken)
nupude_rida1.pack(pady=5)

tk.Button(nupude_rida, text="Kuva kontaktid", command=kuva_kontaktid,font=("Haettenschweiler",14),fg="black", bg="pink").pack(side="left",pady=0)
tk.Button(nupude_rida, text="Lisa kontakt", command=lisa_kontakt_gui,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida, text="Otsi kontakt", command=otsi_kontakt_gui,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida, text="Kustuta kontakt", command=kustuta_kontakt_gui,font=("Haettenschweiler",14),fg="black", bg="pink").pack(side="left")
tk.Button(nupude_rida, text="Sorteeri kontakt", command=sorteeri_gui,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida1, text="Sorteeri Z–A", command=sorteeri_tagurpidi_gui,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida, text="Muuda kontakt", command=muuda_kontakt_gui,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida1, text="Kontaktide arv", command=kuva_kontaktide_arv,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida1, text="Tühjenda väljad", command=puhasta_valjad,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida1, text="Näita e-mailid", command=kuva_emailid,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida1, text="Otsi e-maili", command=otsi_email_gui,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")
tk.Button(nupude_rida1, text="Saada kiri", command=saada_kiri_aken,font=("Haettenschweiler",14),fg="black",  bg="pink").pack(side="left")

tekstikast = tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)

aken.mainloop()
