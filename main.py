import numpy as np
from readData import readData
from calcNRMSD import calcNRMSD
from calcTrendLine import calcTrendLine
from writeData import writeData

folder = "C:\\Users\\lucas\\OneDrive\\Doutorado\\Artigos\\Grating-modeling\\periodico\\calibration\\data"
name = "CLB_H_15E-2_DT_5E-5_DP_1875E-6"
columnHeight = 0.15
tinitial = 5.0
Cs = [0.5, 0.75, 1.0, 2.0, 5.0]
Cs_sufix = ["5E-1","75E-2","1E+0","2E+0","5E+0"]

data = []
for i in range(len(Cs)):
    presFile = folder + "\\" + name + "_CS_" + Cs_sufix[i] + "_pressure.txt"
    waveFile = folder + "\\" + name + "_CS_" + Cs_sufix[i] + "_wave.txt"

    presData = readData(presFile, 1, [1,2], tinitial)
    waveData = readData(waveFile, 1, [1,2], tinitial)

    waveNrmsd = calcNRMSD(waveData, columnHeight)
    presStd = np.std(presData[1])/np.mean(presData[1])

    data.append([]) 
    data[i] = [Cs[i], presStd, waveNrmsd]

trendData = calcTrendLine(data, 0.1)

stdFile = folder + "\\" + name + "_Std.txt"
trendLineFile = folder + "\\" + name + "_TrendLine.txt"

writeData(stdFile, data)
writeData(trendLineFile, trendData)