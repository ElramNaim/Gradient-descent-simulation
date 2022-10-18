from predictValue import predictValue
import numpy as np
import pandas as pd

def computeErrors(Data,Y,Hypothesis):
    Errors=[]
    #if Data and Y are the same length
    if Data.shape[0]==Y.shape[0]:
        for x in range(Data.shape[0]):
            #use predict value
            value=predictValue(Data[x],Hypothesis)
            #appened to error vector
            Errors.append(value-Y[x])
        return Errors
    else: print("there not the same size!") 
    return




       