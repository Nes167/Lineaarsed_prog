while True:
    try:
        isikukood=input("Isikukood:")
        if isikukood.isdigit() and len(isikukood)==11:
            ik_list=list(isikukood)
            if int(ik_list[0]) in [1,3,5]:
                sugu="mees"
            elif int (ik_list[0]) in [2,4,6]:
                sugu="naine"
            else:
                print("esimene sümbol ei ole õige")
                continue #Начать запрос заново
            print("2-7 s. kontroll")
            if int(ik_list[1]+ik_list[2]) in range (0,100):
                print("2,3 sümbolid on ok")
                #!!! aasta=
                if int(ik_list[3]+ik_list[4]) in range(1,13):
                    print("4,5 sümbolid on ok")
                    if int(ik_list[5]+ik_list[6]) in range(1,32) and int(ik_list[3]+ik_list[4]) in range(1,13,2) or int(ik_list[5]+ik_list[6]) in range(1,31) and int(ik_list[3]+ik_list[4]) in range(4,13,2) or int(ik_list[5]+ik_list[6]) in range(1,30) and int(ik_list[3]+ik_list[4])==2:
                        print("6,7 sümbolid on ok")
                        print("Kontrollnumber")
                        # summa=0
                        # for i, s in enumerate(ik_list): #i=0,1,2,3,4,5... s="3","12"...
                        #     summa+=(i+1)+int(s)
                        aste1=[1,2,3,4,5,6,7,8,9,]
                        aste2=[3,4,5,6,7,8,9,1,2,3]
                        ik_n_list=[] #[4,7,6,1,0,2,3,4,5]
                        for s in range(ik_list):
                            ik_n_list.append(int(s))
                    else:
                        print("6,7 sümbolid ei ole ok ")
                        continue
                else:
                    print("4,5 sümbolid ei ole ok ")
                    continue
            else:
                 print("2,3 sümbolid ei ole ok ")
                 continue
        else:
            print("Isikukood on numbrid: ")
    except:
        print("Viga andmetega")
