# ﻿a=0
# while a!=0: #!= -не равно
#    print(a)
#    a=int(input("a: "))
# while True:
#      print(a)
#      a=int(input("a: "))
#      if a==100: break  
# print()
# for i in range(0,10,1):
#     print(f"{i+1}. samm")
# print()
# for i in range(1,11):
#     print(f"{i}. samm")

#Ulesanne 1
# while True:
#     try:
#         nimi=input("Mis on sinu nimi: ")
#         if nimi.isalpha(): break
#     except:
#         print("Viga!")
# while True:
#     try: 
#         k=int(input("Mitu korda tervitada? ")) #k.isnumeric
#         if k>0: break
#     except:
#         print("Viga!")  

# #1. variant
# i=0
# while True:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i}. korda")
#     if i==k: break

# #2. variant
# i=0
# while i<k:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i}. korda")

# #3. variant
# print("For")
# for i in range(1,k+1):
#     print(f"Ole tervitatud, {nimi}, {i}. korda")
    
# #Ulesanne 2
# summa=0
# i=0
# while i<10:
#     a=float(input(f"Sisesta {i+1} number: "))
#     summa +=a
#     i +=1
#     print("Sisestatud arvude summa: ,summa")

# #1. variant
# summa=0
# j=0
# while True:
#     while True:
#         try:
#             a=float(input("a: "))
#             break
#         except:
#             print("Viga!")
#     summa+=a
#     j+=1
#     if j==10:break  
# print(f"Arvude summa: {summa}")

# #2. variant
# summa=0
# while True:
#     number=input("Sisesta arv (vajuta Enter lõpetamiseks): ")
#     if number=="":break
#     try:
#         number=float(number)
#         summa +=number
#     except:
#         print("Viga!")
# print(f"Arvude summa: {summa}")

# #3. variant
# summa=0
# for i in range(10):
#     while True:
#         try:
#             a=float(input(f"Sisesta {i+1} number:"))
#             summa += a     
#         except:
#             print("Viga!")
# print(f"Arvude summa: {summa}")

# #Ulesanne 3
# from random import *
# tehete_arv=2
# min_arv=1
# max_arv=50
# õiged_vastused=0
# for _ in range(tehete_arv):
#     arv1=random.randint(min_arv,max_arv)
#     arv2=random.randint(min_arv,max_arv)
#     õiged_vastused=arv1+arv2
#     print(f"Mitu on {arv1}+{arv2}?")
#     katsete_arv=5
#     while katsete_arv>0:
#         try:
#             kasutaja_vastus=int(input("Teie vastus: "))
#             if kasutaja_vastus==õiged_vastused:
#                 print("Õige vastus!")
#                 õiged_vastused+=1
#                 break
#             else:
#                 katsete_arv-=1
#                 if katsete_arv>0:
#                     print("Vale vastus!")
#                 else:
#                     print(f"Õige vastus oli: {õiged_vastused}")
#         except:
#             print("Palun sisestage arv!")
# print(f"Mäng läbi! Sa vastasid õigesti {õiged_vastused}/{tehete_arv} tehet.")

# #Ulesanne 4

# #1.variant
# for i in range(1,11):
#     print(i)
# print()

# #2.variant
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}={i*j}")
# print()

# #3.variant
# for i in range(1,11):
#      print(f"{i}")

# Ulesanne 5
# N=int(input("N: "))
# for j in range(N):
#     for i in range(N):
#         if i==j or i+j==N-1:
#             print("X",end=" ")
#         else:
#             print("O",end=" ")
#     print()
# print()

# #Ulesanne 6
# for i in range(5):
#     print("*"*5)

# for i in range(1,5):
#     print("*"*i)
    
# for i in range(5,0,-1):
#     print("*"*i)

# #Ulesanne 7
# from random import *
# N=1
# for i in range(5):
#     N*=10
#     print(N)
#     N+=randint(0,9)
#     print(N)

# #Ulesanne 8
# paaris=0
# paaritu=0
# for number in range(1,101):
#     if number %2==0:
#         print(f"{number}on paaris")
#         paaris+=1
#     else:
#         print(f"{number}on paaritu")
#         paaritu+=1
# print(f"Paaris arve kokku:{paaris}")
# print(f"Paaritu arve kokku:{paaritu}")

# #Ulesanne 9
# for i in range(1,11):
#     print(f"{i}*5={i*5}")

# #Ulesanne 10
# for arv in range(1,101):
#     if arv %5==0:
#         print(arv)

# #Ulesanne 11
# from random import *
# arv = random.randint(1, 100)
# for i in range(3):
#     kasutaja_arvamus = int(input("Arva arv ära (1-100): "))
#     if kasutaja_arvamus == arv:
#         print("Õnnitleme, arvasid õige arvu ära!")
#         break
#     else:
#         if i < 2:  
#             print("Vale arv. Proovi veel.")
#         else: 
#             print(f"Õnnetuseks ei saanud sa õiget arvu kätte. Õige arv oli {arv}.")

# #Ülesanne 13
# print(f"{'Arv':<5}{'Ruut':<6}{'Kuup':<6}")
# print("-"*20)

# for arv in range(1, 11):
#     ruut = arv**2
#     kuup = arv**3
#     print(f"{arv:<5}{ruut:<6}{kuup:<6}")

# #Ülesanne 14
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i * j:4}", end=" ")
#     print()

# #Ülesanne 15
# katseid =0
# while True:
#     vastus = input("Osta elevant ära! ").strip().lower()
#     katseid +=1
#     if vastus == "elevant":
#         break
# print(f"Tubli! Sa ostsid elevandi {katseid} katsega.")

# #Ülesanne 18
# N = 3
# M = 7
# for arv in range(N, M + 1):
#     print(f"{arv} {arv ** 2} {arv ** 3}", end=" ")
# print()

# #Ülesanne 22
# loendur = 0
# while True:
#     sisend = input("Tahan kommi! ").strip().lower()
#     loendur += 1
#     if sisend == "komm":
#         print(f"Aitäh! Palusin kommi {loendur} korda.")
#         break


# #Ülesanne 23
# n = int(input("Mitu õpilast on rühmas? "))
# tais_ealised = 0
# alaealised = 0
# for i in range(n):
#     vanus = int(input(f"Sisesta {i+1}. õpilase vanus: "))
#     if vanus >= 18:
#         tais_ealised += 1
#     else:
#         alaealised += 1
# print(f"Täisealisi õpilasi: {tais_ealised}")
# print(f"Alaealisi õpilasi: {alaealised}")