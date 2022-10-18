import numpy as np

def computeGradient(Data,Errors):
    Gradient=[]
    for x in range(Data.shape[1]):
         #multyply each value^j(i) by the errors(i)
         value=Data[:,x] *Errors
         #sum the values of each col
         sum=np.sum(value)
         #divide in 100 (m)
         sum/=100
         #appened to gradient vector
         Gradient.append(sum)
    return Gradient



