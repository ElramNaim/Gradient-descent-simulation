import numpy as np

def predictValue(Example,Hypothesis):
    #multyply matrix
    value=np.dot(Example,Hypothesis)
    return value

       