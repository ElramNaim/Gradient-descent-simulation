


def updateHypothsis(Hypothesis, alpha, Gradient):
    #size of Hypothesis
    size=len(Hypothesis)
    updateHypothsis=[]
    # calculate and appened to update Hypothesis
    for x in range(size):
        updateHypothsis.append((Hypothesis[x]-alpha*Gradient[x]))
    return updateHypothsis
