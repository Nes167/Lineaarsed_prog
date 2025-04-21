from random import *
sonad = [
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]
def tolkija(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            return kirje[siht]
    return "Sõna ei leitud!"

def lisa_sona(sonad):
    print("Lisame uue sõna sõnastikku!")
    uus_est = input("Sisesta sõna eesti keeles: ").strip().lower()
    uus_rus = input("Sisesta sõna vene keeles: ").strip().lower()
    uus_eng = input("Sisesta sõna inglise keeles: ").strip().lower()
    sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
    print("Uus sõna on lisatud!")

def loo_sonastik():
    return sonad

def vali_keelte_suund():
    print("Sisesta keelte suund:")
    allikas=input("Sisesta allikakeel est/eng/rus: ").lower()
    siht=input("Sisesta sihtkeel est/eng/rus: ").lower()
    return allikas, siht

def otsi_sona(sonad, sona):
    for k in sonad:
        if sona in k.values():
            return k

def paranda_sona(sonad):
    sona=input("Sisesta sõna parandamiseks: ").lower()
    k=otsi_sona(sonad, sona)
    if k:
        print(f"Leitud {k} ")
        k['est']=input("Uus eesti keeles: ").lower()
        k['rus']=input("Uus vene keeles: ").lower()
        k['eng']=input("Uus inglise keeles: ").lower()
        print("Sõna on parandatud")
        print(sonad)
    else:
        print("Sõna ei leitud")


def testi_teadmisi(sonad):
    allikas, siht = vali_keelte_suund()
    õige=0
    kus_vas = {}
for rida in sonad:
    kysimus, vastus = rida.split(':')
    kus_vas[kysimus.strip()] = vastus.strip()
kysimused=list(kus_vas.keys())
while True:
    n=randint(0, len(sonad)-1)
    valitud_kysimus=kysimused[n]
    print(valitud_kysimus)
    vastus=input("Sisesta vastus: ")
    if kus_vas[valitud_kysimus].lower()==vastus.lower():
        print("Õige vastus")
        õige += 1
    elif kus_vas[valitud_kysimus].lower()==0:
        break
    else:
        print("Vale vastus")
    # for _ in range (5):
    #     kirje=random.choice(sonad)
    #     vastus=input("Sisesta vastus: ")
    #     if vastus==kirje[siht]:
    #         print("Õige vastus")
    #         õige +=1
    #     else:
    #         print(f"Vale vastus. Õige on {kirje[siht]}")
    # print(f"Tulemus: {õige}/5")

def kuva_sonad(sonad):
    for k in sonad:
        print(k)