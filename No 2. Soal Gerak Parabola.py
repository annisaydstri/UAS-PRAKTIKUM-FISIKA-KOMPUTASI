import numpy as np
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier

# Database: Gerbang logika AND
# x = Data, Y = Sumbu, t = waktu
x = [[1,0], [10,0], [15,0],[20,0],[25,0]]
y = [20.0,40.0,60.0,80.0,100.0]
t = [5,10,20,25,30]

# Training and Classify
clf = MLPClassifier(solver='lbfgs', alpha=1e-2, hidden_layer_sizes=(10, 5), random_state=1, max_iter=1000, warm_start=True)
clf.fit(x,y)
# Prediksi
print ("Logika AND Metode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("1 0 = ", clf.predict([[20, 0]]))
print ("2 0 = ", clf.predict([[40, 0]]))
print ("3 0 = ", clf.predict([[60, 0]]))
print ("4 0 = ", clf.predict([[80, 0]]))
print ("4 0 = ", clf.predict([[100, 0]]))


alpha = np.radians(45)
g = 9.8
v0 = 1.4*(10**(-3))
x0,y0 = 0,0

v0x = v0*np.cos(alpha)
v0y = v0*np.sin(alpha)

X = ((v0**2)*np.sin(2*alpha))/(2*g)
print("Jarak Horizontal Maksimum = ",X," m")
Y = ((v0*2)*(np.sin(alpha)**2))/(2*g)
print("Jarak Vertikal Maksimum = ",Y," m")
T = (2*v0*np.sin(alpha))/g
print ("Waktu Mencapai Jarak Horizontal Maksimum = ",T," s")
print("\n")

t = np.arange(0.0, T, 10**(-6))
y = v0y*t - 0.5*g*t**2
x = v0x*t

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x (m)', ylabel= 'y (m)' , title='Grafik Gerak Parabola')
ax.grid()
plt.show()
