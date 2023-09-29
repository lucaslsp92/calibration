import numpy as np

def calcNRMSD(data, reference):
    n = len(data[1])
    sum = 0.0
    for i in range (n):
        sum += pow((data[1][i]-reference), 2.0)
    nrmsd = np.sqrt(sum/(n-1))/reference
    return nrmsd