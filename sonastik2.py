import random
# import pyttsx3  #Импортируем библиотеку для синтеза речи


def sonad_failist(fail):
    sonad=[]
    with open(fail,'r',encoding="utf-8-sig") as f:
        for rida in f:
            est,rus,eng=rida.strip().split(",")
            sonad.append({'est':est,'rus':rus,'eng':eng})
    return sonad

def salvesta_sonad(fail,sonad):
    with open(fail,'w',encoding="utf-8-sig") as f:
        for k in sonad:
            f.write(f"{k['est']},{k['rus']},{k['eng']}\n")

def valjasta_tervitus():  #Приветствие при запуске программы
    print("Tere tulemast keelesõnastikku!")


def kuva_menu():
    """Меню выбора
    """
    print("Menu:")
    print("1 - Tõlgi sõna\n2 - Lisa uus sõna \n3 - Paranda sõna\n4 - Kuva kõik sõnad\n5 - Testi teadmisi\n6 - Tekst kõneks\n0 - Välja")


def tolkija(sonad, allikas, siht, sona):
    """Функция перевода слова с одного языка на другой
    """
    for kirje in sonad: #Перебираем каждую запись в словаре
        if kirje[allikas] == sona.lower(): #Если слово найдено в выбранном языке
            return kirje[siht] #Возвращаем перевод
    return "Sõna ei leitud!"


def lisa_sona(sonad):
    """Добавление нового слова в словарь
    """
    print("Lisame uue sõna sõnastikku!") #Запрашиваем слово на всех трёх языках, маленькими буквами и убираем лишние пробелы
    uus_est = input("Sisesta sõna eesti keeles: ").strip().lower()
    uus_rus = input("Sisesta sõna vene keeles: ").strip().lower()
    uus_eng = input("Sisesta sõna inglise keeles: ").strip().lower()
    sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng}) #Добавляем словарь в список
    print("Uus sõna on lisatud!")

def loo_sonastik():
    return sonad
    """ Возвращает текущий словарь
    """

def vali_keelte_suund():
    """Функция выбора языка. из какого в какой
    """
    print("Sisesta keelte suund:")
    allikas=input("Sisesta allikakeel est/eng/rus: ").lower() #из какого
    siht=input("Sisesta sihtkeel est/eng/rus: ").lower() #в какой
    return allikas, siht


def paranda_sona(sonad):
    """Исправление слова
    """
    parandatav=kysi_kasutajalt_sisestus("Sisesta parandatav sõna: ")  #Запрашиваем у пользователя слово для исправления через функцию kysi_kasutajalt_sisestus
    kirje=otsi_sona(sonad, parandatav)  #Используем функцию otsi_sona для поиска слова в словаре
    if kirje:  #Если слово найдено
        kirje['est']=kysi_kasutajalt_sisestus("Uus eesti sõna: ")  #спрашиваем новые переводы через функцию
        kirje['rus']=kysi_kasutajalt_sisestus("Uus vene sõna: ")  
        kirje['eng']=kysi_kasutajalt_sisestus("Uus inglise sõna: ")  
        print("Parandatud!") 
    else:
        print("Sõna ei leitud!")  #Если слово не найдено

def kysi_kasutajalt_sisestus(tekst):
    """Запрашиваем ввод от пользователя и проверяем, что он не пустой
    """
    while True:
        sisend=input(tekst).lower()  #Запрашиваем ввод, маленькими буквами
        if sisend=="":  #Если строка пустая
            print("Tühja ei tohi jätta!")  #то пишем что нельзя оставить пустой
        else:
            return sisend  #Возвращаем введённое слово

def otsi_sona(sonad, sona):
    """Ищет слово во всех значениях словаря и возвращает его запись
    """
    for k in sonad:  #Перебираем все записи в словаре
        if sona in k.values():  #Если слово найдено в любом из языков
            print(f"Leitud sõna: {k}")  #Показываем найденное слово и все переводы
            return k  #Возвращаем слово
    return None  #Если слово не найдено


def testi_teadmisi(sonad):
    """Проверка знаний
    """
    allikas, siht=vali_keelte_suund() #Получаем языки перевода
    õige=0
    kogus=int(input("Mitu sõna soovite kontrollida? ")) #Запрашиваем количество слов
    for _ in range(kogus): #Повторяем нужное число раз
        kirje=random.choice(sonad) #Выбираем рандомные слова
        vastus=input(f"Tõlgi {kirje[allikas]}: ").lower()
        if vastus==kirje[siht]: #Сравниваем с правильным
            print("Õige vastus")
            õige +=1
        else:
            print(f"Vale vastus. Õige on {kirje[siht]}")
    kuva_tulemus(õige, kogus)

def kuva_tulemus(õige, kogus):
    """Вывод результата после проверки знаний
    """
    print(f"Sinu tulemus: {õige}/{kogus}") #Выводим, сколько правильных из всех

def kuva_sonad(sonad):
    """Показывает все слова в словаре
    """
    for k in sonad: #Перебираем и печатаем каждое слово
        print(k)


def text_to_speech():
    mootor = pyttsx3.init() #Инициализация "голоса"
    sona = input("Sisesta sõna: ").lower() #Запрашиваем слово
    mootor.say(sona) #Озвучиваем его
    mootor.runAndWait() #Запускаем произношение