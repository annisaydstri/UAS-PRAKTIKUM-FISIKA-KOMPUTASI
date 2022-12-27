#from sklearn import neural svm
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Database
FileDB = 'riemann.txt'
Database = pd.read_csv(FileDB, sep =",", header=0)
print ("------------------")
print (Database)

#x = data, y = Target 
x = Database[['a,b,Target']] #ciri1, ciri2, dst
y = Database.Target 
#Fit model regresi
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_rbf.fit(x,y)
#Menampilkan data prediksi
xx= np.arange(1, 21, 1)# (data pertama, data terakhir, rentang)
n  = len (xx)
print ("---------------------")
print ("----Prediksi SVM-----")
print ("xx(i) rbf")
for i in range (n):
    rbf = svr_rbf.predict([[xx[i]]])
    print ('{:.2f}'.format(xx[i]), rbf)

#Plot data prediksi
rbf2 = svr_rbf.predict(x)
plt.figure()
plt.plot(x, rbf2, color = 'red')
plt.scatter (x,y, color ='blue')
plt.title ('Prediksi Data Menggunakan SVM')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['rbf', 'data'], loc=2)
plt.show()
