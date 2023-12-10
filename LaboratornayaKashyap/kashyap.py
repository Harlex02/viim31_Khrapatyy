import numpy as np
import matplotlib
import matplotlib.pyplot as plt

k=0
a = []
a = np.genfromtxt('input.txt', delimiter=' ')
print(a)

for point in a:
    if point[2]==-1:
        point[0]=-point[0]
        point[1]=-point[1]
print (a)

a_plus=np.linalg.matrix_power(a.T.dot(a), -1).dot(a.T)
print(a_plus)
y_0=np.ones(a_plus.shape[1])
a_0=a_plus.dot(y_0)
print(a_0)
x=np.array([0,6])
y = -(a_0[0]*x + a_0[2]) / a_0[1]


plt.plot(x, y, color='black')

x_coords = []
y_coords = []
colors=[]
for point in a:
    if point[2]==-1:
        x_coords.append(-point[0])
        y_coords.append(-point[1])
        colors.append('red')
    else:
        x_coords.append(point[0])
        y_coords.append(point[1])
        colors.append('blue')
       
plt.scatter(x_coords, y_coords, c=colors)

plt.show()