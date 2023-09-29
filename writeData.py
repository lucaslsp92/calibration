def writeData(fullFileName, data):
    file = open(fullFileName, "w")
    header = "Cs\t\tStd[P]\t\t\tNRMSD[H]"
    file.write(header)
    for i in range(len(data)):
        file.write("\n{:.2f}\t{:.10f}\t{:.10f}\t".format(data[i][0], data[i][1], data[i][2]))
    file.close()
    return