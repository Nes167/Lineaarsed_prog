# #Ülesanne 1
# try:
#     arv=input("Sisesta arv: ")
#     if arv.isnumeric():
#         arv=int(arv)
#         if arv>0:
#             if arv%2==0 and arv!=0:
#                 print(f"Arv {arv} on paaris.")
#             elif arv==0:
#                 print(f"Arv {arv} on määramatu.")
#             else:
#                 print(f"Arv {arv} on paaritu.")
#         else:
#             print(f"Arv {arv} on negatiivne")
# except:
#     print("Kirjuta numbreid")

# #Ülesanne 2
# try:
#     nurk1=float(input("Sisesta arv: "))
#     nurk2=float(input("Sisesta arv: "))
#     nurk3=float(input("Sisesta arv: "))
#     if nurk1>0 and nurk2>0 and nurk3>0:
#         print("Nurgad on positiivsed")
#         if nurk1+nurk2+nurk3==180:
#             print("See on kolmnurk")
#             if nurk1==nurk2 and nurk2==nurk3 and nurk1==nurk3:
#                 print("võrgkülgne kolmnurk")
#             elif nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
#                 print("võrdhaarne kolmnurk")
#             else:
#                 print("erikülgne kolmnurk")
#         else:
#             print("See ei ole kolmnurk")
#     else:
#         print("Negatiivsed nurgad ei soobi")
# except:
#     print("Sisesta ujukomaarvud!")

# #Ülesanne 3
# try:
#     a=input("Kas soovite dešifreerida nädalapäeva järjekorranumbrit nimesse.").lower()
#     if a=="jah":
#         try:
#             b=int(input("Sisesta nädalapäevanumber: "))
#             if b in range (1,8):
#                 if b==1:
#                     print("esmaspäev")
#                 elif b==2:
#                     print("teisipäev")
#                 elif b==3:
#                     print("kolmapäev")
#                 elif b==4:
#                     print("neljapäev")
#                 elif b==5:
#                     print("reede")
#                 elif b==6:
#                     print("laupäev")
#                 elif b==7:
#                     print("pühapäev")
#         except:
#             print("Numbrid vahemikust 1-7")
#     else:
#         print("ok")
# except:
#     print("Viga! on vaja vastus JAH või EI")

#Ülesanne 4
päev=int(input("Sisesta sünnipäev: "))
kuu=int(input("Sisesta kuu: "))
if kuu==3 and päev==21 or kuu==4 and päev<=19:
    märk="Jäär"
elif kuu==4 and päev==20 or kuu==5 and päev<=20:
    märk="Sõnn"
elif kuu==5 and päev==21 or kuu==6 and päev<=21:
    märk="Kaksikud"
elif kuu==6 and päev==22 or kuu==7 and päev<=22:
    märk="Vähk"
elif kuu==7 and päev==23 or kuu==8 and päev<=22:
    märk="Lõvi"
elif kuu==8 and päev==23 or kuu==9 and päev<=22:
    märk="Neitsi"
elif kuu==9 and päev==23 or kuu==10 and päev<=22:
    märk="Kaalud"
elif kuu==10 and päev==23 or kuu==11 and päev<=21:
    märk="Skorpion"
elif kuu==11 and päev==22 or kuu==12 and päev<=21:
    märk="Ambur"
elif kuu==12 and päev==22 or kuu==1 and päev<=19:
    märk="Kaljukits"
elif kuu==1 and päev==20 or kuu==2 and päev<=18:
    märk="Veevalaja"
elif kuu==2 and päev==19 or kuu==3 and päev<=20:
    märk="Kalad"

print(f"Sa oled {märk}")
