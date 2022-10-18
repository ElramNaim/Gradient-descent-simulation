import numpy as np
import pandas as pd

def normalizePrices(D):
    df = pd.DataFrame(D)
    #div first col by 1000
    df[0] = df[0].div(1000)
    D=df
    return D

def addOnesColumn(D):
    #number of rows
    number=D.shape[0]
    #create new col of 1 with 100 rows
    X0 = np.ones((number,1))
    #add to D
    D = np.hstack((X0,D))
    return D



