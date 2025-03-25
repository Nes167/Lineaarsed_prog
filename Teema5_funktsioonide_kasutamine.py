#Ülesanne 1

def arithmetic(arv1:float, arv2:float, tehe:str)-> any:
    """
    Funktsioon töötab nagu lihtne kalkulaator:
    + liitmine
    - lahutamine
    * korrutamine
    / jagamine
    Kui sisend ei ole järjendis [+, -, *, /], siis tagastab sõne "Tundmatu tehe."
    :param float arv1: Sisend ujukomaarvu tüübina
    :param float arv2: Sisend ujukomaarvu tüübina
    :param str tehe: Sisend listlist [+,-,*,/]
    :rtype: varMääramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0, ei tohi nulliga jagamine"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe."
    return vastus

#Ülesanne2
def is_year_leap(aasta:int)->bool:
    """ Liigiaasta leidmine
    Tagastab True, kui aasta on liigiaasta ja False kui aasta on tavaline.
    :param int aasta: Sisend kasutajalt 
    :rtype: bool tõeväärsuses formaadis tulemus
    """

    if aasta%4==0:
        v=True
    else:
        v=False
    return v



