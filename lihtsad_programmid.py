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
a=(3 +8) / (4 +2) * 4
print(a)