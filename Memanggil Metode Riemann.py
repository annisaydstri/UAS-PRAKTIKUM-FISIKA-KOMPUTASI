import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return np.exp(-5*x)
a = float(input('Batas Bawah(a) = '))
b = float(input('Batas Atas(b)  = '))
n = int(10)
# Metode Riemann
x = np.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0
for i in range(n-1):
    hasil += dx*func(x[i])
print('Hasil = ', hasil)
xp =np.linspace(a,b)
plt.plot(xp,func(xp))
for i in range (n-1):
    plt.bar(x[i],func(x[i]), align = 'edge',width=dx, color = 'blue', edgecolor='black')
plt.show()
