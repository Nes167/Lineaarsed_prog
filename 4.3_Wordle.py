from random import *
o=-1
sõnad=["maja","arvuti","kala","laev","auto","koer","kass","hiir","kuvar"]
salasõna=choice(sõnad)
salasõnalist=list(salasõna)
print(salasõna)
k=len(salasõna)
print("_ "*k)
p=6
tähestik=list("abcdefghijklmnopqrstuvwxyzõäöü")
while p>0:
    print("_ "*k)
    print(f"On jäänud {p} katset")
    p-=1
    sõna=input("Sisesta oma variant: ").lower()
    sõnalist=list(sõna)
    for a in range (0,k,1):
        o+=1
        if sõnalist[0]==salasõnalist[0]:
            print(sõnalist[0],end=" ")
        else:
            print("*",end=" ")
    print()
    if sõna==salasõna:
        print("Huraa!")
        break
    else:
        print("Vale sõna!" ,6-p-1, "on jäänud katset.")
        p-=1
        sõnalist=sõnalist.append(sõna)
        print(sõnalist)


