import numpy as np

def calcTrendLine(data, step):
    xn = np.linspace(data[0][0], data[-1][0], int((data[-1][0]-data[0][0])/step))
    
    cs = []
    pres = []
    wave = []
    for i in range(len(data)):
        cs.append(data[i][0]) 
        pres.append(data[i][1]) 
        wave.append(data[i][2]) 

    presCoeff = np.polyfit(cs, pres, 2)
    waveCoeff = np.polyfit(cs, wave, 2)
    presYn = np.poly1d(presCoeff)
    waveYn = np.poly1d(waveCoeff)
    
    trendData = []
    for i in range(len(xn)):
        trendData.append([]) 
        trendData[i] = [xn[i], presYn(xn[i]), waveYn(xn[i])]
    return trendData