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
        except:
            print("Kirjuta ainult tähtede kasutades!")
        i.append(nimi)
        p.append(palk)


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
    """Самая большая зарплата и кто ее получает
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
    """Самая маленькая зарплата и кто ее получает
    """
    min_palk=min(p)
    print(f"Väiksem palk on {min_palk}")
    k=p.count(min_palk)
    ind=p.index(min_palk)
    for j in range(k):
        ind=p.index(min_palk,ind)
        print(f"Väiksem palk on {min_palk} ja selle saab {i[ind]}")
        ind=ind+1
