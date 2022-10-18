from normalizePrices import normalizePrices,addOnesColumn
from loadData import loadData
from computeErrors import computeErrors
from computeGradient import computeGradient
from updateHypothsis import updateHypothsis
from computeCost import computeCost
import numpy as np
import matplotlib.pyplot as plt


def gradientDescent(filename, alpha=0.1, max_iter=1000,iter=1,threshold=0.001):
    cost_j=float('inf')
    #vector of costs
    Costs=[] 
    #vecotr of iteration
    Iters=[]
    Costs.append(cost_j)   
    #use the loadData method
    D,Y=loadData(filename)
     #normalize the Prices in D
    D=normalizePrices(D)
     #add Ones Column to D 
    D=addOnesColumn(D)
    #make Hypothesis of zeroes
    Hypothesis=[0] * D.shape[1]
     #compute Errors 
    Errors=computeErrors(D,Y,Hypothesis)
    # compute Cost 
    cost_j=computeCost(D,Y,Hypothesis)
    Costs.append(cost_j)
     #compute Gradient 
    Gradient=computeGradient(D,Errors)
    #update the Hypothsis
    Hypothesis=updateHypothsis(Hypothesis,alpha,Gradient)
    #end of first iteration
    iter+=1
    #appened to iteration vector
    Iters.append(iter)
    while iter <= max_iter and Costs[iter-2]-Costs[iter-1] > threshold:
         #compute  new error
        Errors=computeErrors(D,Y,Hypothesis)
        # compute new Cost 
        cost_j=computeCost(D,Y,Hypothesis)
        Costs.append(cost_j)
        #compute new Gradient 
        Gradient=computeGradient(D,Errors)
        Hypothesis=updateHypothsis(Hypothesis,alpha,Gradient)
        iter+=1
        Iters.append(iter)
        if iter>max_iter:
          print("Gradient descent terminating after 1000 iterations (max_iter)")
        if Costs[iter-2]-Costs[iter-1]<threshold:
           print("Gradient descent terminating after", iter ,
           "iterations. Improvement was : ", Costs[iter-2]-Costs[iter-1] ,"below threshold (0.001)")
    FinalHypothesis=Hypothesis
    return FinalHypothesis,Costs,Iters

FinalHypothesis,Costs,Iters=gradientDescent('smartphones.txt')
#we start the iteration from 1 so we dont need the infinity anymore
del Costs[0]
plt.scatter(Iters, Costs, color= "green")
plt.xlabel('iter ')
plt.ylabel('Costs')
plt.show()
