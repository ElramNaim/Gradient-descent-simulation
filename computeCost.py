from computeErrors import computeErrors
import numpy as np

def computeCost(Data,Y,Hypothesis):
    #calclute error
    Errors=computeErrors(Data, Y, Hypothesis)
    #sqaure all the values
    SqaureErr=np.square(Errors)
    #sum all the values
    sumErrors=np.sum(SqaureErr)
    #divide in m*2 (100*2)
    cost=sumErrors/200
    return cost
