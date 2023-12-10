import numpy as np
import matplotlib.pyplot as plt

def get_data(num):

    data = [] 
    label = [] 
    x1 = np.random.normal(2, 0.8, int(num / 2))
    y1 = np.random.normal(2, 0.8, int(num / 2)) 
    x2 = np.random.normal(6, 0.8, int(num / 2))
    y2 = np.random.normal(6, 0.8, int(num / 2)) 
    for i in range(num):
        if i < num / 2:
            data.append([x1[i], y1[i]])
            label.append(-1)
        else:
            data.append([x2[int(i - num / 2)], y2[int(i - num / 2)]])
            label.append(1)
    return data, label



def perceptron(data, label, e):
    w = [0.,1.0] 
    b = 0
    separated = False 
    while not separated:
        separated = True
        for i in range(len(data)):
            if label[i] * (w[0] * data[i][0] + w[1] * data[i][1] + b) <= 0:
                separated = False 
                w[0] += e * label[i] * data[i][0]
                w[1] += e * label[i] * data[i][1]
                b += e * label[i] 
    slope = -w[0] / w[1]    
    intercept = -b / w[1]   
    return slope, intercept

def plot(data, label, slope, intercept):

    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel('X')
    plt.ylabel('Y')
    area = np.pi * 2 ** 2   

    data_mat = np.array(data)
    X = data_mat[:, 0]
    Y = data_mat[:, 1]
    for i in range(len(label)):
        if label[i] > 0:
            plt.scatter(X[i].tolist(), Y[i].tolist(), s=area, color='red')     
        else:
            plt.scatter(X[i].tolist(), Y[i].tolist(), s=area, color='green')
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals)
    plt.show()

data, label = get_data(100) 
slope, intercept = perceptron(data, label, 1) 
plot(data, label, slope, intercept)

   
