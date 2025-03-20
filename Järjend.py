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
# for a in range (5): #Запрос пяти имён у пользователя.
#     nimi=input("Sisesta nimi: ")
#     nimed.append(nimi)
# nimed.sort() #Сортировка в порядке убывания
# print(nimed)
# print(nimed[-1]) #Отдельно вывод последнего введённого имени
# muuda=input("Kas soovite nimi muuta? jah/ei ").lower() #Спросить если хотите поменять имя.
# if muuda == "jah": #Если да, то
#     vana_nimi=input("Mis nimi te soovite muuta?: ") #Спросить какое имя заменить
#     if vana_nimi in nimed:
#         uus_nimi=input("Sisesta uus nimi: ") #Спросить новое имя
#         ind=nimed.index(vana_nimi)
#         nimed[ind]=uus_nimi
#         nimed.sort() #Повторная сортировка по алфавиту
#         print(f"Uuendatud nimed: {nimed}") #Показать обновлённый список имён.
#     else:
#         print("Sellist nime loendis ei ole") #Если имени нет в списке, то выводит сообщение, что такого имени там нет.
# else:
#     print("ok") #Если человек не хочет изменять имя, то написать ОК

# #2.2
# kord_opilased=["Juhan","Kati","Mario","Mario","Mati","Mati"] 
# print(kord_opilased) #Показывается несколько имён, среди них есть повторяющиеся.
# opilased=list(set(kord_opilased))  #Удаление дублирующихся имён
# print(opilased) #Вывод имён без повторов

# #2.3
# vanus=5,13,25,9,20,17,11,10,8,24
# print(vanus) #вывод возрастов
# min_vanus=min(vanus) #Показывает самый минимальный из этого списка
# print(f"\nKõige noorem on {min_vanus}")
# max_vanus=max(vanus) #максимальный возраст из списка
# print(f"Kõige vanem on {max_vanus}")
# summa=sum(vanus) #Сумма всех возрастов
# print(f"Vanuste summa on {summa}")
# keskmine=summa/len(vanus) #средний возраст
# print(f"Keskmine vanus on {keskmine}")

# #Ulesanne 3
# sisend=[8,12,25,38,67,15,48] 
# for number in sisend: #Используем значения чисел в списке и создаём гистограмму, используя звезды.
#     print('*' *number)

# #Ülesanne 4
# region={"1":"Tallinn","2":"Narva, Narva-Jõesuu","3":"Kohtla-Järve","4":"Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","5":"Tartu linn", "6":"Tartumaa, Põlvamaa, Võrumaa, Valgamaa","7":" Viljandimaa, Järvamaa, Harjumaa, Raplamaa","8": "Pärnumaa","9":"Läänemaa, Hiiumaa, Saaremaa"} #Список со значениями, если 1 то Таллинн, если 2 то Нарва, Нарва-Йыесуу, если 3 то Кохтла-Ярве и т.д.
# post_indeks=input("Sisestage postiindeks: ") #Просит ввести индекс
# if post_indeks.isdigit() and len(post_indeks) == 5: #проверяет что состоит только из цифр и длина только 5 цифр
#     maakond=region.get(post_indeks[0]) #смотрит какой первый символ вводит пользователь и проверяет в словаре.
#     print(f"Teie postiindeks kuulub piirkonda: {maakond}") #выводит к какому региону относится индекс
#     if post_indeks[0] in ["1","2","3"]:
#         print("Olge kodus") #если индекс начинается с 1,2 или 3, то говорит остаться дома
#     else:
#         print("Kandke maske!") #на все остальные говорит носить маску
# else:
#     print("Vigane sisend!") #если такого региона нет в словаре,то ошибка ввода

# #Ülesanne 9
# from string import *
# vokaali=["a","o","e","i","u","ü","õ","ä","ö"]
# konsonanti="qwrtypsdfghjklzxcvbnm"
# v=k=0
# nimi=input("Sisestage nimi: ") #Вводим имя
# if nimi.isalpha(): #проверем чтобы только из букв
#     nimi=nimi.capitalize() #первую букву заглавную
#     print(f"tere, {nimi}") 
#     nimi_pikkus=len(nimi) #считаем количество символов
#     print(f"nimi pikkus on {nimi_pikkus}")
#     for s in nimi: #считаем гласные и согласные в имени
#         if s in vokaali:
#             v+=1
#         elif s in konsonanti:
#             k+=1
#     print(f"Vokaali: {v} \nKonsonanti: {k}")
#     sort_tahed="".join(sorted(set(nimi.lower()))) #сортируем буквы по алфавиту, исключаем повторения букв
#     print(f"Tähed tähestikulises järjekorras {sort_tahed}")
# else:
#     print("Viga! Peab sisaldama ainult tähti") #если имя введено не только из букв, то выдаём ошибку

# #ülesanne 11
# import string
# n=int(input("Sisestage tähtede arv: ")) #Запрашиваем количество букв
# tähed=list(string.ascii_lowercase[:n]) #добавляются в список все строчные буквы английского алфавита, берётся столько символов сколько введёт пользователь
# korduvad_tähed=[] #создаём список с повторяющимися буквами
# for i in range(n):
#     korduvad_tähed.append(tähed[i]*(i+1)) #в цикле повторяется, в зависимости от позиции и добавляется в список
# print("Järjend:", tähed) #буквы которые мы используем
# print("Teine järjend:", korduvad_tähed) #те же буквы, но повторяются взависимости от позиции

# #12 ülesanne
# import random
# numbrid = [random.randint(1, 100) for s in range(10)] # Создаем список из 10 случайных чисел от 1 до 100
# print(f"Loend: {numbrid}")
# min_index = numbrid.index(min(numbrid)) # Находим индексы минимального элемента
# max_index = numbrid.index(max(numbrid)) # Находим индексы максимального элемента
# numbrid[min_index], numbrid[max_index] = numbrid[max_index], numbrid[min_index] # Меняем местами минимальный и максимальный элементы
# print(f"Loend pärast vahetamist: {numbrid}")

# #Ülesanne 17
# sõna_list=["auto","jalgrattas","laev","lennuk","rong","buss","tramm"] #список транспорта
# leia_sõna=input("Milline transport te otsite? ").lower() #спрашиваем какой транспорт ищем, сразу делаем маленькими буквами
# leitud_sõna=[s for s in sõna_list if leia_sõna in s.lower()] #проверяем содержится это слово в нашем списке
# if leitud_sõna: #если слово содержится, то выдаем, что оно там есть
#     print(f"Sõna {leia_sõna} on leitud")
# else:
#     print(f"Sõna {leia_sõna} ei ole loendis") #если слово не содержится в списке 
