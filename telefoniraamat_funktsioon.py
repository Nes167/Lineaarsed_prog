import smtplib,ssl
from email.message import EmailMessage

def loefailist(fail:str):
    telefoniraamat=[]
    with open(fail,'r',encoding="utf-8-sig") as f:
        for rida in f:
            nimi,email,telefon=rida.strip().split(",")
            telefoniraamat.append({'nimi':nimi,'email':email,'telefon':telefon})
    return telefoniraamat

def Kirjutafailisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

def salvesta_sonad(fail,sonad):
    with open(fail,'w',encoding="utf-8-sig") as f:
        for k in telefoniraamat:
            f.write(f"{k['nimi']},{k['email']},{k['telefon']}\n")

def lisa_kontakt(telefoniraamat):
    """Добавление нового контакта в телефонную книгу
    """
    print("Lisame uue kontakti!") #Добавляем новый контакт
    uus_nimi = input("Sisesta nimi: ").strip().capitalize()
    uus_email = input("Sisesta e-mail: ").strip().lower()
    uus_telefon = input("Sisesta telefoninumber: ").strip()
    telefoniraamat.append({'nimi': uus_nimi, 'email': uus_email, 'telefon': uus_telefon}) #Добавляем в список
    print("Uus kontakt on lisatud!")
    Kirjutafailisse(telefoniraamat)

def kuva_kontaktid(telefoniraamat):
    """Показывает все контакты в телефонной книге
    """
    for k in telefoniraamat: #Перебираем и печатаем каждый контакт
        print(k)

def otsi_kontakt(telefoniraamat, nimi):
    """Ищет слово во всех значениях словаря и возвращает его запись
    """
    for n in telefoniraamat:  #Перебираем все записи в книге контактов
        if nimi in n.values():  #Если слово найдено в любом из языков
            print(f"Leitud: {n}")  #Показываем найденное имя и все данные
            return n  #Возвращаем имя
    return None  #Если имя не найдено

def paranda_kontakt(telefoniraamat):
    """Исправление контакта
    """
    parandatav=input("Sisesta parandatav andmed: ").lower()  #Запрашиваем данные которые нам надо изменить
    kirje=otsi_kontakt(telefoniraamat, parandatav)  #Используем функцию otsi_kontakt для поиска данных в книге контактов
    if kirje:  #Если слово найдено
        kirje['nimi']=input("Uus nimi: ")  #спрашиваем новые данные
        kirje['email']=input("Uus email: ")  
        kirje['telefon']=input("Uus telefon: ")  
        print("Parandatud!") 
    else:
        print("Ei leitud!")  #Если не найдено
    Kirjutafailisse(telefoniraamat)

def kistuta_kontakt(telefoniraamat, nimi, email, telefon):
    """ Удалить контакт
    """
    try:
        kustutav=input("Sisesta kustutav nimi: ").capitalize()
        kirje=otsi_kontakt(telefoniraamat, kustutav) #Используем функцию otsi_kontakt для поиска данных в книге контактов
        if k>0:
            for j in range(k):
                ind=nimi.index(nimi)
                nimi.pop(ind)
                email.pop(ind)
                telefon.pop(ind)
            print("Andmed on kustutatud!")
        else:
            print("Andmed on puuduvad!")
    except:
        print("Kirjuta ainult tähtede kasutades!")
    kustutav=input("Sisesta kustutav nimi: ")
    kirje=otsi_kontakt(telefoniraamat, kustutav)  #Используем функцию otsi_kontakt для поиска данных в книге контактов
    Kirjutafailisse(telefoniraamat)

def sorteeri_kontakt(telefoniraamat, by):
    print("Sorteerimise valikud: nimi / email / telefon")
    by=input("Sisesta valik: ")
    if by in ["nimi", "telefon", "email"]:
        if by=="nimi":
            telefoniraamat.sort(key=nimi_key)
            return kontakt["nimi"].capitalize()
        if by=="email":
            telefoniraamat.sort(key=email_key)
            return kontakt["email"].lower()
        if by=="telefon":
            telefoniraamat.sort(key=telefon_key)
            return kontakt["telefon"]
        print("Kontaktid on sorditud.")
    else:
        print("Tundmatu sorterimisviis.")

def saada_kiri():
    kellele=input("Kellele: ")
    kiri="""<!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<h2>Sending an HTML email from Python</h2>
<p>Hello there,</p>
<a href="https://inspirezone.tech/">Here's a link to an awesome dev
community!</a>
</body>
</html>"""
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="anastassiamayba@gmail.com"
    parool=input("Rakenduste parool") #gjfk fbvi nfjk hoyu
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele

    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print('Kiri saadetud')
    except Exception as e:
        print("Viga: ", e)