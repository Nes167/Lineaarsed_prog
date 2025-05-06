import matplotlib.pyplot as plt
import numpy as np

# 1. Failist lugemine
linnad = []
rahvaarvud = []

with open("rahvaarv.txt", encoding="utf-8") as f:
    for rida in f:
        osad = rida.strip().split()
        linn = " ".join(osad[:-1])
        arv = int(osad[-1])
        linnad.append(linn)
        rahvaarvud.append(arv)

# 2. NumPy array töötluseks
arvud_np = np.array(rahvaarvud)

# 3. Statistika
koguarv = arvud_np.sum()
keskmine = arvud_np.mean()
suurim = arvud_np.max()
väikseim = arvud_np.min()
suurima_linn = linnad[np.argmax(arvud_np)]
väikseima_linn = linnad[np.argmin(arvud_np)]

# 4. Tulemuste printimine
print(f"Koguarv: {koguarv}")
print(f"Keskmine: {keskmine:.1f}")
print(f"Suurim: {suurima_linn} ({suurim})")
print(f"Väikseim: {väikseima_linn} ({väikseim})")

# 5. Tulpdiagramm
plt.figure(figsize=(10, 6))
plt.bar(linnad, rahvaarvud, color="skyblue")
plt.title("Eesti linnade rahvaarv")
plt.xlabel("Linn")
plt.ylabel("Elanike arv")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

x=np.arange(-10,10,1)# -10,-9,-8....10  linspace(-10,10,100)-punktidearv
y=2*x**2-4*x+5
plt.figure(facecolor='yellow')
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("2*x**2-4*x+5")
plt.title("Graafik")
plt.grid()
plt.savefig('graafik.png')
plt.show()

#babochka

x=np.linspace(-9, -1, 100)#y
y=-1/8*(x+9)**2+8

x1=np.linspace(1, 9, 100)#b
y1=-1/8*(x1-9)**2+8

x2=np.linspace(-9,-8,100)#y
y2=7*(x2+8)**2+1

x3=np.linspace(8,9,100)#b
y3=7*(x3-8)**2+1

x4=np.linspace(-8,-1,100)#y
y4=1/49*(x4+1)**2

x5=np.linspace(1,8,100)#b
y5=1/49*(x5-1)**2

x6=np.linspace(-8,-1,100)#l
y6=(-4/49)*(x6+1)**2

x7=np.linspace(1,8,100)#p
y7=(-4/49)*(x7-1)**2

x8=np.linspace(-8,-2,100)#l
y8=1/3*(x8+5)**2-7

x9=np.linspace(2,8,100)#p
y9=1/3*(x9-5)**2-7

x10=np.linspace(-2,-1,100)#l
y10=-2*(x10+1)**2-2

x11=np.linspace(1,2,100)#p
y11=-2*(x11-1)**2-2

x12=np.linspace(-1,1,100)
y12=-4*x12**2+2

x13=np.linspace(1,-1,100)
y13=4*x13**2-6

x14=np.linspace(-2,0,100)
y14=(-1.5)*x14+2

x15=np.linspace(0,2,100)
y15=1.5*x15+2

plt.plot(x, y, linestyle='-', marker='o', color='yellow')
plt.plot(x1, y1, linestyle='-', marker='o', color='blue')
plt.plot(x2, y2, linestyle='-', marker='o', color='yellow')
plt.plot(x3, y3, linestyle='-', marker='o', color='blue')
plt.plot(x4, y4, linestyle='-', marker='o', color='yellow')
plt.plot(x5, y5, linestyle='-', marker='o', color='blue')
plt.plot(x6, y6, linestyle='-', marker='o', color='lightblue')
plt.plot(x7, y7, linestyle='-', marker='o', color='pink')
plt.plot(x8, y8, linestyle='-', marker='o', color='lightblue')
plt.plot(x9, y9, linestyle='-', marker='o', color='pink')
plt.plot(x10, y10, linestyle='-', marker='o', color='lightblue')
plt.plot(x11, y11, linestyle='-', marker='o', color='pink')
plt.plot(x12, y12, linestyle='-', marker='o', color='red')
plt.plot(x13, y13, linestyle='-', marker='o', color='red')
plt.plot(x14, y14, linestyle='-', marker='o', color='red')
plt.plot(x15, y15, linestyle='-', marker='o', color='red')
plt.grid()
plt.savefig('babochka.png')
plt.show()


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, linestyle='--', marker='o', color='red',markersize=8,  markeredgecolor='yellow', markerfacecolor='lightblue')
plt.title("Lihtne graafik")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.show()

plt.scatter(x, y, color='lightblue', label='Punktidest diagramm')
plt.legend()
plt.show()

plt.bar(x, y, color='pink', label='Tulpdiagramm')
plt.legend()
plt.show()

plt.hist(x, y, color='red', label='Histogramm')
plt.legend()
plt.show()

# plt.pie(x, y, color='red')
# plt.show()