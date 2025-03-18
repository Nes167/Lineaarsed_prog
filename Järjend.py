# sõne="Programmeerimine"
# print(sõne)
# list_sõne=list(sõne)
# print(list_sõne)
# print(f"Viies täht: {list_sõne[4]}")
# print(f"Sõnes on {len(sõne)} t")

# #append
# elemendid=[]
# for i in range(5):
#     elemendid.append(input(f"{i+1}. element: ")) #Добавляет элемент в конец списка
# print(elemendid)
# for e in elemendid:
#     print(e)

# #extend
# list_sõne.extend(elemendid) #Расширяет список list_sõne, добавляя в конец все элементы списка elemendid
# print(list_sõne)
# print(elemendid)

# #insert
# elemendid.insert(0,"A")
# print(elemendid) #Вставляет на 0-ой элемент значение A

# #remove
# elemendid.remove("A") #Удаляет первый элемент в списке, имеющий значение A
# print(elemendid)

# #pop
# elemendid.pop(0) #Удаляет 0-oй элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# elemendid.pop()
# print(elemendid)

# #index
# ind=list_sõne.index("r") #Возвращает положение первого элемента от start до end со значением r
# print(f"Täht r on {ind}-indeksiga")

# #count
# k=list_sõne.count("r") #Возвращает количество элементов со значением r
# print(f"Täht r kohtume {k} korda sõnas {sõne}")

# #sort
# list_sõne.sort(reverse=True) #Сортирует список на основе функции. Если reverse - true, то Z-A, если false, то наоборот
# print(list_sõne)

# #reverse
# list_sõne.sort() #Разворачивает список
# print(list_sõne)

# #copy
# list_sõne2=list_sõne.copy() #Копия списка

# #clear
# list_sõne2=list_sõne.clear() #Очищает список

# #Ülesanne 1
# from string import *
# vokaali=["a","o","e","i","u","ü","õ","ä","ö"]
# konsonanti="qwrtypsdfghjklzxcvbnm"
# numbrid=digits
# märkid=punctuation
# v=k=n=m=t=0
# tekst=input("Sisend sõna või lause: ").lower()
# tekst_list=list(tekst)
# if tekst_list.index(" ")>0:
#     print("See on lause")
#     for s in tekst_list:
#         if s in vokaali:
#             v+=1
#         elif s in konsonanti:
#             k+=1
#         elif s in numbrid:
#             n+=1
#         elif s in märkid:
#             m+=1
#         elif s==" ":
#             t+=1
#     print(f"Vokaali: {v} \nKonsonanti: {k} \nNumbrid: {n} \nMärkid: {m} \nTühik: {t}")
# else:
#     print(f"kokku on {len(tekst_list)}")
#     if s in vokaali:
#             v+=1
#     elif s in konsonanti:
#         k+=1
#     print(f"Vokaali: {v} \nKonsonanti: {k}")

# #Ülesanne 2
# #2.1
# nimed=[]
# for a in range (5):
#     nimi=input("Sisesta nimi: ")
#     nimed.append(nimi)
# nimed.sort()
# print(nimed)
# print(nimed[-1])
# muuda=input("Kas soovite nimi muuta? jah/ei ").lower()
# if muuda == "jah":
#     vana_nimi=input("Mis nimi te soovite muuta?: ")
#     if vana_nimi in nimed:
#         uus_nimi=input("Sisesta uus nimi: ")
#         ind=nimed.index(vana_nimi)
#         nimed[ind]=uus_nimi
#         nimed.sort()
#         print(f"Uuendatud nimed: {nimed}")
#     else:
#         print("Sellist nime loendis ei ole")
# else:
#     print("ok")

# #2.2
# kord_opilased=["Juhan","Kati","Mario","Mario","Mati","Mati"]
# print(kord_opilased)
# opilased=list(set(kord_opilased))
# print(opilased)

# #2.3
# vanus=5,13,25,9,20,17,11,10,8,24
# print(vanus)
# min_vanus=min(vanus)
# print(f"\nKõige noorem on {min_vanus}")
# max_vanus=max(vanus)
# print(f"Kõige vanem on {max_vanus}")
# summa=sum(vanus)
# print(f"Vanuste summa on {summa}")
# keskmine=summa/len(vanus)
# print(f"Keskmine vanus on {keskmine}")

# #Ülesanne 4
# region={"1":"Tallinn","2":"Narva, Narva-Jõesuu","3":"Kohtla-Järve","4":"Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","5":"Tartu linn", "6":"Tartumaa, Põlvamaa, Võrumaa, Valgamaa","7":" Viljandimaa, Järvamaa, Harjumaa, Raplamaa","8": "Pärnumaa","9":"Läänemaa, Hiiumaa, Saaremaa"}
# post_indeks=input("Sisestage postiindeks: ")
# if post_indeks.isdigit() and len(post_indeks) == 5:
#     maakond=region.get(post_indeks[0])
#     print(f"Teie postiindeks kuulub piirkonda: {maakond}")
#     if post_indeks[0] in ["1","2","3"]:
#         print("Olge kodus")
#     else:
#         print("Kandke maske!")
# else:
#     print("Vigane sisend!")

