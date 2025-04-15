from random import *

def sisesta_andmed():
    """Ввод данных. имена пациентов и генерация Д-витамина
    :return: Списки с именами и значениями витамина Д
    """
    nimed = []  #Список для имён пациентов
    d_vitamiin = []  #Список для значений витамина D

    try:
        kogus = int(input("Mitu patsienti soovid sisestada? "))  #Сколько пациентов ввести?
        if kogus < 0:
            print("Palun sisesta positiivne arv.")  #Сообщение, если число не положительное
            return [], []
        for i in range(kogus):#Вводим имена по одному
            nimi = input(f"Sisesta patsiendi nr {i+1} nimi: ").capitalize()  #Ввод имени
            nimed.append(nimi)  #Добавляем имя в список
            d_tase = randint(10, 80)  #Рандом уровень Д-витамина от 10 до 80
            d_vitamiin.append(d_tase) #Добавляем значение в список
        return nimed, d_vitamiin  #Возвращаем списки
    except:
        print("Viga! palun sisesta täisarv.")  #Сообщение об ошибке, если введено не число
        return [], []


def puudus_vitamiin_d(nimed, d_vitamiin):
    """ Функция для отображения пациентов с недостатком витамина Д (<30)
    :param list nimed: Список имён пациентов
    :param list d_vitamiin: Список значений витамина Д
    """
    print("Patsiendid, kellel on D-vitamiini puudus (<30):")
    leitud = False
    for i in range(len(nimed)):
        if d_vitamiin[i] < 30:  #Проверяем уровень
            print(f"{nimed[i]} : {d_vitamiin[i]} mcg/l")  #Выводим результат у кого недостаток Д витамина
            leitud = True
    if not leitud:
        print("Kõik patsiendid on normaalsel tasemel.")  #Если ни у кого нет дефицита


def keskmine_vitamiin_d(d_vitamiin):
    """Функция для расчёта и вывода среднего значения витамина Д
    :param list d_vitamiin: Список значений витамина Д
    """
    summa = sum(d_vitamiin) #Складываем все значения
    keskmine = summa / len(d_vitamiin) #Делим на количество
    print("Keskmine D-vitamiini tase:", round(keskmine, 2), "mcg/l") #Выводим результат
    return keskmine


def top_k_vitamiin_d(nimed, d_vitamiin):
    """Топ K пациентов по уровню витамина Д
    :param list nimed: Список имён пациентов
    :param list d_vitamiin: Список значений витамина Д
    """
    try:
        k = int(input("Mitu parimat patsienti soovid näha? "))  #Сколько лучших хотим увидеть
        if k <= 0:
            print("Palun sisesta positiivne arv.")
            return
        top = sorted(zip(nimed, d_vitamiin), reverse=True)[:k] #Объединяем имена и значения. Сортируем в порядке убывания и берём столько имён сколько ввёл пользователь
        print("Parimad patsiendid:")
        for nimi, d_tase in top:
            print(f"{nimi} : {d_tase}")
    except:
        print("Palun sisestage korrektne arv!")

 
def otsi_patsiendi_vitamiin_d(nimed, d_vitamiin):
    """Поиск пациента по имени и вывода его уровня Д
    :param list nimed: Список имён пациентов
    :param list d_vitamiin: Список значений витамина Д
    """
    nimi = input("Sisesta patsiendi nimi, keda otsid: ").capitalize()  #Запрашиваем имя для поиска
    leitud = False
    for i in range(len(nimed)): #Перебираем список и ищем имя, которое ввёл пользователь
        if nimed[i]==nimi:
            print(f"{nimed[i]} : {d_vitamiin[i]} mcg/l")
            leitud = True
    if not leitud:
        print("Sellist patsienti ei leitud.")  # Если не найдено

def alla_keskmise(nimed, d_vitamiin):
    """Показывает пациентов у которых уровень Двитамина ниже среднего.
    :param list nimed: Список имён пациентов
    :param list d_vitamiin: Список значений витамина Д
    """
    keskmine = keskmine_vitamiin_d(d_vitamiin)
    print("Patsiendid alla keskmise:")
    alla=zip(nimed, d_vitamiin)
    for nimi, d_tase in alla: #Ищем пациентов c значением ниже среднего
        if d_tase < keskmine:
            print(f"{nimi}: {d_tase} mcg/l")

