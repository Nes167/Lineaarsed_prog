
# haigla={
#     range(1,10):"Kuressaare Haigla",
#     range(11,19):"Tartu Ülikooli Naistekliinik, Tartumaa, Tartu",
#     range(21,220):"Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
#     range(221,270):"Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
#     range(271,370):"Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla",
#     range(371,420):"Narva Haigla",
#     range(421,470):"Pärnu Haigla",
#     range(471,490):"Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla",
#     range(491,520):"Järvamaa Haigla (Paide)",
#     range(521,570):"Rakvere, Tapa haigla",
#     range(571,600):"Valga Haigla",
#     range(601,650):"Viljandi Haigla",
#     range(651,700):"Lõuna-Eesti Haigla (Võru), Põlva Haigla"
#     }
while True:
    try:
        isikukood=input("Sisesta isikukood: ")
        if isikukood.isdigits() and len(isikukood)==11:
            ik_list=list(isikukood)
            if int(ik_list[0]) in [1,3,5]:
                sugu="mees"
            elif int(ik_list[0]) in [2,4,6]:
                sugu="naine"
            else:
                print("Esimene sümbol ei ole õige")
                continue
            print("2-7 kontroll")
            #!!! aasta=...
            if ik_list[1]+ik_list[2] in range(0,100):
                print("2,3 sümbolid on ok")
                if ik_list[3]+ik_list[4] in range(1,13):
                    print("4,5 sümbolid on ok")
                    if ik_list[5]+ik_list[6] in range(1,32) and int(ik_list[3]+ik_list[4]) in range(1,13,2) or ik_list[5]+ik_list[6] in range(1,31) and int(ik_list[3]+ik_list[4]) in range(4,13,2) or ik_list[5]+ik_list[6] in range(1,30) and int(ik_list[3]+ik_list[4])==2:
                        print("6,7 sümbolid on ok")
                        print("kontrollnumber")
                        summa=0
                        for i, s in enumerate(ik_list): #i=0,1,2,3,4,5... s="3","12"...
                            summa+=(i+1)+int(s)
                    else:
                        print("ei ole ok")
                        continue
                else:
                    print("ei ole ok")
                    continue
            else:
                print("ei ole ok")
                continue
        else:
            print("Viga! isikukood peab olema ainult numbridest ja peab olema 11 arvu.")
    except:
        "Viga andmetega"