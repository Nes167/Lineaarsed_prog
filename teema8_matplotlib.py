# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(-10,10,1)# -10,-9,-8....10  linspace(-10,10,100)-punktidearv
# y=2*x**2-4*x+5
# plt.figure(facecolor='yellow')
# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("2*x**2-4*x+5")
# plt.title("Graafik")
# plt.grid()
# plt.savefig('graafik.png')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-9,-1,1)
y=(-1/8)*((x+9)**2)+8

x1=np.arange(1,9,1)
y1=(-1/8)*((x-9)**2)+8

x2=np.arange(-9,-8,1)
y2=7*((x+8)**2)+1

x3=np.arange(8,9,1)
y3=7*((x-8)**2)+1

x4=np.arange(-8,-1,1)
y4=(1/49)*(x+1)**2

x5=np.arange(1,8,1)
y5=(1/49)*(x-1)**2

x6=np.arange(-8,-1,1)
y6=(-4/49)*(x+1)**2

x7=np.arange(1,8,1)
y7=(-4/49)*(x-1)**2

x8=np.arange(-8,-2,1)
y8=(1/3)*((x+5)**2)-7

x9=np.arange(1,8,1)
y9=(1/3)*((x-5)**2)-7

x10=np.arange(-2,-1,1)
y10=-2*((x+1)**2)-2

x11=np.arange(1,2,1)
y11=-2*((x-1)**2)-2

x12=np.arange(-1,1,1)
y12=-4*x**2+2

x13=np.arange(1,-1,1)
y13=4*x**2-6

x14=np.arange(-2,0,1)
y14=-1,5*x+2

x15=np.arange(0,2,1)
y15=1,5*x+2

plt.plot(x, y, linestyle='-', marker='o', color='red')
plt.plot(x1, y1, linestyle='-', marker='o', color='blue')
plt.plot(x2, y2, linestyle='-', marker='o', color='red')
plt.plot(x3, y3, linestyle='-', marker='o', color='red')
plt.plot(x4, y4, linestyle='-', marker='o', color='red')
plt.plot(x5, y5, linestyle='-', marker='o', color='red')
plt.plot(x6, y6, linestyle='-', marker='o', color='red')
plt.plot(x7, y7, linestyle='-', marker='o', color='red')
plt.plot(x8, y8, linestyle='-', marker='o', color='red')
plt.plot(x9, y9, linestyle='-', marker='o', color='red')
plt.plot(x10, y10, linestyle='-', marker='o', color='red')
plt.plot(x11, y11, linestyle='-', marker='o', color='red')
plt.plot(x12, y13, linestyle='-', marker='o', color='red')
plt.plot(x14, y14, linestyle='-', marker='o', color='red')
plt.plot(x15, y15, linestyle='-', marker='o', color='red')
plt.show()









# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x, y, linestyle='--', marker='o', color='red',markersize=8,  markeredgecolor='yellow', markerfacecolor='lightblue')
# plt.title("Lihtne graafik")
# plt.xlabel("x telg")
# plt.ylabel("y telg")
# plt.show()

# plt.scatter(x, y, color='lightblue', label='Punktidest diagramm')
# plt.legend()
# plt.show()

# plt.bar(x, y, color='pink', label='Tulpdiagramm')
# plt.legend()
# plt.show()

# plt.hist(x, y, color='red', label='Histogramm')
# plt.legend()
# plt.show()

# plt.pie(x, y, colors=['gray','yellow','red','blue','pink']
# plt.legend()
# plt.show()