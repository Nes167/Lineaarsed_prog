from datetime import *
from calendar import *
from math import *
from time import strptime
#Ülesanne 1
tana=date.today() 
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)

# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)

# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(tana3)

# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)

päev=tana.day
kuu=tana.month
aasta=tana.year

print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")

paevad=monthrange(2025,2)[1]
onjaanud=paevad-päev
print(f"kuu lõpuni on jäänud {onjaanud} päevad")

paev1=monthrange(2025,2)[1]
paev2=monthrange(2025,3)[1]
paev3=monthrange(2025,4)[1]
paev4=monthrange(2025,5)[1]
paev5=monthrange(2025,6)[1]
paev6=monthrange(2025,7)[1]
paev7=monthrange(2025,8)[1]
paev8=monthrange(2025,9)[1]
paev9=monthrange(2025,10)[1]
paev10=monthrange(2025,11)[1]
paev11=monthrange(2025,12)[1]
onjaanud=paev1+paev2+paev3+paev4+paev5+paev6+paev7+paev8+paev9+paev10+paev11
print(f"Aasta lõpuni on jäänud {onjaanud} päevad")
try:
    sunnipaev=input("Sünnipaev: ") #DD/MM/YYYY
    sp=datetime.strptime(sunnipaev,"%d/%m/%Y")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades * 12
    vanus_paevades=(tana-sp.date()).days
    print(f"Sinu vanus aastades on {vanus_aastades} ")
    print(f"Sinu vanus kuudes on {vanus_kuudes} ")
    print(f"Sinu vanus päevades on {vanus_paevades} ")
except:
    print("sa pead DD/MM/YYYY format kasutada sisestamisel")

#Ülesanne 2
#Sulgude kasutamine
print("a=3 +8/ (4 - 2) * 4")
a=3 + 8 / (4 - 2) * 4
print(a)
print("a=(3 + 8)/ (4 - 2) *4")
a=(3 +8) / (4 - 2) * 4
print(a)
print("a=3 + 8 / 4 - 2 * 4")
a=3 + 8 / 4 - 2 * 4
print(a)
print("a=(3 + 8) / 4 - 2 * 4")
a=(3 + 8) / 4 - 2 * 4
print(a)
print("a=(3 + 8 / 4) - 2 * 4")
a=(3 + 8 / 4) - 2 * 4
print(a)

#ülesanne 3

try:
    R=float(input("Sisesta R, kus R on ringi raadius: "))
    # == kas võrdub, != ei võrdu, < rohkem, > vähem, <= rohkem või võrdne, >= vähem või võrdne
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
    else:
        Ringi_S=round(pi*R**2,2)
        Ringi_P=round(2*pi*R,2)
        Ruudu_S=round(2*R*2*R,2)
        Ruudu_P=round(2*R*4,2)
        print(f"Ringi_S= {Ringi_S} \nRingi_P= {Ringi_P} \nRuudu_S= {Ruudu_S} \nRuudu_P= {Ruudu_P} ")
except: 
    print("Sisesta ainult arvud!!!")

#Ülesanne 4
maa_R_km=6378
münte_d=22.75
maa_R_mm=maa_R_km*1000000
maa_p=2*pi*maa_R_mm
münte_arv=round(maa_p/münte_d)
print(f"On vaja {münte_arv} münte.")

#Ülesanne 5
a="kill koll".capitalize()
b="killadi-koll".capitalize()
print(a, a, b, a, a, b, a, a, a, a)

#ülesanne 6
t="""
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(t.upper())

#Ülesanne 7
a=float(input("Sisesta ristküliku esimese külje pikkus: "))
b=float(input("Sisesta ristküliku teise külje pikkus: "))
ümbermõõt=2*(a+b)
pindala=a*b
print(f"Ristküliku ümbermõõt on {ümbermõõt}, ja pindala on {pindala}.")

#Ülesanne 8
kütus_litr=float(input("sisesta tangitud kütuse kogus: "))
läbitud_km=float(input("sisesta läbitud km: "))
if läbitud_km>0:
    kütuse_kulu=kütus_litr/läbitud_km*100
    print(f"keskmine kütusekulu on {kütuse_kulu} liitrit.")
else:
    print(f"viga: läbitud km arv peab olema suurem kui 0.")

#Ülesanne 9
kiirus_kmh=29.9
minutid=float(input("Sisesta aeg rulluisutamisel: "))
vahemaa_km=round(kiirus_kmh/60*minutid,3)
print(f"rulluisutaja läbib {minutid} minutiga {vahemaa_km} km.")

# #Ülesanne 10
minutid_kasutajalt=int(input("Aeg minutides: "))
tunnid=minutid_kasutajalt//60 #täisosa
minutid=minutid_kasutajalt%60 #jääk
print(f"{tunnid}:{minutid}".center(20,"+")) 

