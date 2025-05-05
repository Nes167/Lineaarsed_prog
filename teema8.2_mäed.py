import matplotlib.pyplot as plt
import numpy as np

# 1. Failist lugemine
mäed = []
kõrgus = []

with open("maed.txt", encoding="utf-8") as f:
    for rida in f:
        osad = rida.strip().split()
        mägi = " ".join(osad[:-1])
        kõrg = int(osad[-1])
        mäed.append(mägi)
        kõrgus.append(kõrg)

# 2. NumPy array töötluseks
arvud_np = np.array(kõrgus)

# 3. Statistika
koguarv = arvud_np.sum()
keskmine = arvud_np.mean()
suurim = arvud_np.max()
väikseim = arvud_np.min()
suurim_mägi = mäed[np.argmax(arvud_np)]
väikseim_mägi = mäed[np.argmin(arvud_np)]

for n in range(0,len(mäed)):
    for m in range(n,len(mäed)):
        if kõrgus[n]<kõrgus[m]:
            kõrgus[n],kõrgus[m]=kõrgus[m],kõrgus[n]
            mäed[n],mäed[m]=mäed[m],mäed[n]


# 4. Tulemuste printimine
print(f"Kogukõrgus: {koguarv}")
print(f"Keskmine: {keskmine:.1f}")
print(f"Suurim: {suurim_mägi} ({suurim})")
print(f"Väikseim: {väikseim_mägi} ({väikseim})")

# 5. Tulpdiagramm
plt.figure(figsize=(10, 6))
plt.bar(mäed, kõrgus, color="magenta")
plt.title("Maailma mägede kõrgus")
plt.xlabel("Mägi")
plt.ylabel("Kõrgus")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mäed_graafik.png')
plt.show()

