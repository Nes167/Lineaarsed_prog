import tkinter as tk
from tkinter import *
from telefoniraamat_funktsioon import *



fail = "telefoniraamat.txt"
telefoniraamat = loefailist(fail)

# def naita_kontakte():
#     tekstikast.delete(1.0, tk.END)
#     for k in telefoniraamat:
#         tekstikast.insert(tk.END, f"{k['nimi']}, {k['email']}, {k['telefon']}\n")

# def lisa_kontakt_gui():
#     nimi = simpledialog.askstring("Lisa", "Sisesta nimi:").capitalize()
#     email = simpledialog.askstring("Lisa", "Sisesta e-mail:")
#     telefon = simpledialog.askstring("Lisa", "Sisesta telefon:")
#     if nimi and email and telefon:
#         telefoniraamat.append({'nimi': nimi, 'email': email, 'telefon': telefon})
#         naita_kontakte()

# def otsi_kontakt_gui():
#     nimi = simpledialog.askstring("Otsi", "Sisesta nimi:")
#     if nimi:
#         for k in telefoniraamat:
#             if nimi.lower() in k['nimi'].lower():
#                 messagebox.showinfo("Leitud", f"{k['nimi']}, {k['email']}, {k['telefon']}")
#                 return
#         messagebox.showwarning("Ei leitud", "Kontakt puudub.")

# def kustuta_kontakt_gui():
#     nimi = simpledialog.askstring("Kustuta", "Sisesta nimi:")
#     if nimi:
#         for k in telefoniraamat:
#             if nimi.lower() in k['nimi'].lower():
#                 telefoniraamat.remove(k)
#                 naita_kontakte()
#                 messagebox.showinfo("Eemaldatud", "Kontakt kustutatud.")
#                 return
#         messagebox.showwarning("Ei leitud", "Kontakt puudub.")

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

# def saada_email_gui():
#     kellele = simpledialog.askstring("Saada kiri", "Sisesta saaja e-mail:")
#     parool = simpledialog.askstring("Parool", "Sisesta rakenduse parool:", show='*')
#     if kellele and parool:
#         try:
#             smtp_server = "smtp.gmail.com"
#             smtp_port = 587
#             kellelt = "anastassiamayba@gmail.com"
#             msg = EmailMessage()
#             msg['Subject'] = "Tere!!!"
#             msg['From'] = kellelt
#             msg['To'] = kellele
#             msg.set_content("Tere!")
#             context = ssl.create_default_context()
#             server = smtplib.SMTP(smtp_server, smtp_port)
#             server.starttls(context=context)
#             server.login(kellelt, parool)
#             server.send_message(msg)
#             messagebox.showinfo("Edu", "Kiri saadetud!")
#         except Exception as e:
#             messagebox.showerror("Viga", str(e))

# def salvesta_ja_valja():
#     Kirjutafailisse(fail, telefoniraamat)
#     root.destroy()


aken = tk.Tk()
aken.title("Telefoniraamat")
aken.iconbitmap("phonebook.ico")
aken.configure(bg="lightblue")
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
tk.Button(nupude_rida, text="Lisa kontakt", command=lisa_kontakt,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Otsi kontakt", command=otsi_kontakt,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Muuda kontakt", command=paranda_kontakt,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Kustuta kontakt", command=kustuta_kontakt,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Sorteeri_kontakt", command=sorteeri_kontakt,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Saada e-kiri", command=saada_kiri,font=("Rockwell",12),fg="black").pack(side="left")
tk.Button(nupude_rida, text="Salvesta", command=Kirjutafailisse,font=("Rockwell",12),fg="black").pack(side="left")


tekstikast = tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)




aken.mainloop()
