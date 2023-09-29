def readData(fullFileName, headerLines, columns, tinitial):
    data = []           # initialize 3D array
    for _ in range(len(columns)):
        data.append([]) 

    # read the TXT files
    file = open(fullFileName, "r")
    for _ in range(headerLines):                
        line = file.readline()             # skip the header lines

    line = file.readline().strip()          # read the line
    while line:
        if line == "":                      # verifies the line is empty
            break
        values = line.split()               # split the line in whitespace
        if float(values[0]) >= tinitial:
            for j in range(len(columns)):
                col = columns[j]-1
                try:
                    data[j].append(float(values[col]))
                except:
                    print("Failed to read file: ",fullFileName)              
        line = file.readline().strip()      # read the line
    file.close() 

    return data                                 # return the data (list of lists of lists)