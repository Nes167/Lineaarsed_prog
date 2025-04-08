
p=[]
i=[]
def Lisa_andmed(p:list,i:list):
    """ Добавляем несколько людей и зарплат
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk: "))
                except:
                    print("Palk on arv!")
                break
                print("Andmed on lisatud!")
                p.append(palk)
                i.append(nimi)
        except:
            print("Kirjuta ainult tähtede kasutades!")

        
def Kustuta_andmed(p:list,i:list):
    """ Удалить человека и его зарплату
    """
    try:
        nimi=input("Nimi: ")
        if nimi.isalpha():
            k=i.count(nimi)
            if k>0:
                for j in range(k):
                    ind=i.index(nimi)
                    i.pop(ind)
                    p.pop(ind)
                print("Andmed on kustutatud!")
            else:
                print("Andmed on puuduvad!")
    except:
        print("Kirjuta ainult tähtede kasutades!")

def Suurim_palk(p:list,i:list):
    """ Самая большая зарплата и кто ее получает
    """
    max_palk=max(p)
    print(f"Suurim palk on {max_palk}")
    k=p.count(max_palk)
    ind=p.index(max_palk)
    for j in range(k):
        ind=p.index(max_palk,ind)
        print(f"Suurim palk on {max_palk} ja selle saab {i[ind]}")
        ind=ind+1

def Väiksem_palk(p:list,i:list):
    """ Самая маленькая зарплата и кто ее получает
    """
    min_palk=min(p)
    print(f"Väiksem palk on {min_palk}")
    k=p.count(min_palk)
    ind=p.index(min_palk)
    for j in range(k):
        ind=p.index(min_palk,ind)
        print(f"Väiksem palk on {min_palk} ja selle saab {i[ind]}")
        ind=ind+1

def sorteerimine_kasvav(p:list,i:list)->any:
    """ Упорядочить зарплаты в порядке возрастания вместе с именами
    :param p: Список зарплат
    :type p: list
    :param i: Список имён
    :type i: list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def sorteerimine_kahanev(p:list,i:list)->any:
    """ Упорядочить зарплаты в порядке убывания вместе с именами
    :param p: Список зарплат
    :type p: list
    :param i: Список имён
    :type i: list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]<p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def Võrdsed_palgad(p:list,i:list):
    """ Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

def palk_otsimine(p:list,i:list):
    """Сделать поиск зарплаты по имени человека. 
    """
    try:
        nimi=input("Sisesta nimi otsinguks: ")
        leitud=False
        for o in range(len(i)): #проходим по всем индексам
            if i[o]==nimi: #если имя совпадает 
                print(f"{i[o]} saab palka {p[o]}") # написать имя человека и какую зарплату он получает
                leitud=True
            else:
                print("Sellise nimega inimest ei leitud.") # если имени нет в списке
    except:
        print("Viga!")

# def filtr_palgad(p:list,i:list):
#     try:
#         summa=float(input("Sisesta summa mille järgi filtreerida: "))
#         valik=input(f"Kas otsida inimesi, kelle palk on rohkem kui {summa}? ").lower()
#         if valik=="jah":
#             rohkem=True
#         else:
#             rohkem=False
#         valitud_inimesed=[(i[j],p[j]) for j in range(len(p)) if rohkem]

def tulumaks(p:list,i:list):
    """Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.
    """
    palk=float(input("Sisesta palgasumma: "))
    summa=palk*0.78
    km=palk*0.22
    print(f"Netto palk on {summa}. Käibemaks on {km}")



# def top_inimesed(p:list, i:list):
#     """Топ самых бедных и самых богатых человека
#     """
#     maks=

