import numpy as np

def calcCRMSD(data, reference):
    n = len(data[1])
    sum = np.sum(pow((data[1]-meanData)-(reference[1]-meanReference), 2.0))
    crmsd = np.sqrt(sum/n)/stdReference
    return crmsd