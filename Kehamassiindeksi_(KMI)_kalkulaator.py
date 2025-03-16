print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Palun sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
vastus = input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if vastus == "1":  
    try:
        pikkus =int(input("Palun sisesta oma pikkus sentimeetrites: "))  
        mass = float(input("Palun sisesta oma kehakaal kilogrammides: "))
        kmi = round(mass / ((0.01*pikkus)** 2),1)  
        print(f"{nimi}! Sinu keha indeks on: {kmi}")
        if kmi < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= kmi <= 19:
            print("Alakaal")
        elif 20 <= kmi <= 25:
            print("Normaalkaal")
        elif 26 <= kmi <= 30:
            print("Ülekaal")
        elif 31 <= kmi <= 35:
            print("Rasvumine")
        elif 36 <= kmi <= 40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")
    except:
        print("Viga! Palun sisesta numbrilised väärtused.")   
elif vastus == "0":  
    print("Kahju! See on väga kasulik info! \n ")
else:
    print("Viga! Palun sisesta 0 või 1.")
print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
