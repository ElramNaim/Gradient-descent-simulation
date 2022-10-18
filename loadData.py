import numpy as np
import matplotlib.pyplot as plt

def loadData(filename): 
    #number of features + newPrice
    size= np.loadtxt(filename).shape[1]
    #features columns
    D=np.genfromtxt(filename,usecols=np.arange(0, size-1),dtype=float, encoding=None)
    #newprice column
    Y=np.genfromtxt(filename,usecols=size-1,dtype=float, encoding=None)
    #how many lines
    number=np.loadtxt(filename).shape[0]
    print("read" ,number,"rows")
    x, z = D[:, 0], D[:, 1]
    plt.scatter(x, Y, color= "green", marker= "*", s=20)
    plt.xlabel('original price ')
    plt.ylabel('new smartphone price')
    plt.title("1")
    plt.show()
    plt.scatter(z, Y, color= "green",marker= "*", s=20)
    plt.xlabel('age')
    plt.ylabel('new smartphone price')
    plt.title("2")
    plt.show()
    return D,Y



